from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/add/', views.employee_add, name='employee_add'),
    path('employees/delete/<int:pk>/', views.employee_delete, name='employee_delete'),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/mark/', views.attendance_mark, name='attendance_mark'),
]
