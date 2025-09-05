from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)  # creates the session!
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'accounts/login.html')

@login_required
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html', {'user': request.user})

def logout_view(request):
    logout(request)  # clears the session
    return redirect('login')
