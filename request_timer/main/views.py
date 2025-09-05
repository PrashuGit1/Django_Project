from django.shortcuts import render
from django.http import HttpResponse
import time
# Create your views here.

def home(request):
    time.sleep(1)
    return HttpResponse("Hello! This is the home page")
