from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fun1(req):
    return HttpResponse('Hello, I am fun1 from app2')
