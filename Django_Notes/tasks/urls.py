from django.urls import path

from . import views

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


]