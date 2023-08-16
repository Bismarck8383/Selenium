from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks_complete/', views.tasks_completed, name='tasks_complete'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('create/', views.create_task, name='create'),
    path('task/<int:task_id>/', views.task_detail, name='task_id'),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('saludo/', SaludoViews.as_view(), name='saludo'),
    path('nueva/', Nuevo.as_view(), name="nueva"),
    path('last_tasks/', UltimasTareasView.as_view(), name='last_tasks'),
]
