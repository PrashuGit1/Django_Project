from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app1.models import Employee
import json

@csrf_exempt
def create_employee(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        employee=Employee(
            employee_name=data['employeeName'],
            email = data['email'],
            phone = data['phone'],
            hire_date = data['hireDate'],
            job_title = data['jobTitle'],
            employment_type = data['employeeType'],
            salary = data['salary'],            
        )
        Employee.save(employee)

        return JsonResponse({'message': "Employee Saved Succesfully!!"})
        
    
def get_employee(request):
    if request.method == 'GET':
        employees = Employee.objects.values()
        list_result = [entry for entry in employees]
        return JsonResponse(list_result, safe=False)
