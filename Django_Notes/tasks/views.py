from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import *
import datetime
from django.utils import timezone
#vamos a protejer nuestras rutas
from django.contrib.auth.decorators import login_required
from django.views import View

# Create your views here.

def home(request):

    return render(request, 'home.html')



def signup(request):
    if request.method == 'GET':
        context = {
            'mytitle': 'Signup',
            'mensaje': 'Rellene los datos del formulario',
            'form': UserCreationForm,
            'message_color': 'black'
        }
        return render(request, 'signup.html', context)
    else:

        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('signin')

            except IntegrityError:
                context = {
                    'mytitle': 'Signup',
                    'mensaje': 'El usuario ya existe por favor introduzca otro',
                    'form': UserCreationForm,
                    'message_color': 'red'
                }
                return render(request, 'signup.html', context)

        else:

            context = {
                'mytitle': 'Signup',
                'mensaje': 'Las contraseñas no coinciden, intentelo de nuevo por favor',
                'form': UserCreationForm,
                'message_color': 'red'
            }
            return render(request, 'signup.html', context)

@login_required
def tasks(request):
    # la primera filtra solo deja ver tareas sin completar
    tasks = Task.objects.filter(user=request.user, datecomplete__isnull=True)
    #tasks = Task.objects.all() --es para ver todas las tareas
    #tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks.html',{
        'tasks' : tasks
    })

@login_required
def tasks_completed(request):
    tasks = Task.objects.filter(user=request.user, datecomplete__isnull=False)
    return render(request, 'tasks.html', {
        'tasks': tasks
    })

@login_required
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html')
    else:
        print(request.POST)
        user = authenticate(request,username=request.POST['username'], password=request.POST['password'])
        error=''
        color='red'
        if user is None:
            return render(request, 'signin.html', {
                'error': "Username o password is incorrect",
                'color': color
            })
        else:
            login(request,user)
            return redirect('tasks')

@login_required
def create_task(request):
    mensaje=''
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        important = request.POST.get('important') == 'on'

        # Comprueba si los campos 'title' y 'description' están vacíos
        if not title or not description:
            mensaje = 'Error: El título y la descripción no pueden estar vacíos.'
            return render(request, 'createTasks.html', {'error': mensaje})

        user = request.user
        task = Task(title=title, description=description, important=important, user=user)
        task.save()

        return redirect('tasks')

    else:
        return render(request, 'createTasks.html')

@login_required
def task_detail(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        return render(request, '404.html', status=404)
    return render(request, 'task_detail.html', {'task': task})

@login_required
def update_task(request, task_id):
    task = Task.objects.get(pk=task_id)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.important = request.POST.get('important') == 'on'
        task.save()

        return redirect('tasks')

    else:
        return render(request, 'task_detail.html', {'task': task})


@login_required
def complete_task(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("La tarea no existe.")

    if request.method == 'POST':
        task.datecomplete = timezone.now()
        task.save()
        return redirect('tasks')

    return render(request, 'task_detail.html', {'task': task})

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    else:
        return render(request, 'task_detail.html', {'task': task})

class SaludoViews(View):
    def get(self, request):
        return HttpResponse("<h1>Saludando a todas las personas de este site</h1>")


class Nuevo(View):
    def get(self, request):
        return HttpResponse("<h1>Nuevo saludos probando las clases</h1>")


class UltimasTareasView(View):
    def get(self, request):
        # Obtener las últimas tres tareas ordenadas por fecha de creación
        latest_tasks = Task.objects.order_by("-created")[:3]

        # Construir la respuesta HTML
        response_html = "<h1>Últimas tres tareas:</h1>"
        for task in latest_tasks:
            response_html += f"""
                <p>{task.title} - {task.created} - {task.description}</p> 
            """

        return HttpResponse(response_html)