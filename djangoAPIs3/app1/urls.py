from django.contrib import admin
from django.urls import path
from app1.views import create_employee,get_employee

urlpatterns = [
    path('employee/add', create_employee, name='Create Employee'),
    path('employee/all', get_employee, name='Get all Employee'),
]