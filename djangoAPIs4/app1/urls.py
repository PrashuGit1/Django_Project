from django.urls import path
from app1.views import create_employee,get_employee

urlpatterns = [
    path('employee/add',create_employee, name='create_employee'),
    path('employee/all', get_employee, name='get_employee')
]