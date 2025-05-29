from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_name=models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    hire_date = models.DateField()
    job_title = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
