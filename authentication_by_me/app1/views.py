from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login(req):
    if req.method=="POST":
        username=req.POST.get('username')
        password=req.POST.get('password')
        user=authenticate(req, username=username, password=password)

        if user:
            login(req, user)
            return redirect('home')
        else:
            messages.error(req, 'Invalid credentials')

    return render(req, 'app1/login.html')

@login_required
def home(req):
    return render (req, 'app1/home.html')

def dashboard(req):
    return render (req, "dashboard.html")



# Create your views here.
