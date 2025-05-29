from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myfun1(request):
    return HttpResponse("Hello Mr. Welcome tro the home page")

def myfun2(request):
    return HttpResponse("Hello Mr. Welcome tro the first page")