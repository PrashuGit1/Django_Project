from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fun1(req, **kawrgs):
    status=kawrgs.get('status', 'Not applicable')
    return HttpResponse(f"Hello I am Fun1 from Aap1 {status}")
