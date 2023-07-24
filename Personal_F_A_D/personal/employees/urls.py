from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='api'),
    path('create_employee_page/', views.new_employee, name='new_employee'),
    path('add_employee/', views.create_employee, name='add.employee'),
    path('list/', views.employees_list, name='list'),
    path('id/<int:employee_id>', views.get_employee_by_id, name='by_id'),
    path('delete/<int:employee_id>', views.delete_employee_id, name='delete_id'),
    path('update/<int:employee_id>', views.update_employee, name='update_employee'),

]
