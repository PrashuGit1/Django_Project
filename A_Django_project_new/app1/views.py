from django.shortcuts import render
from app1.models import Profile

# Create your views here.

def myapp1(req):

    student=Profile.objects.all()
    print(student)
    return render(req, 'app1/home.html', {'student':student})
