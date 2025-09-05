from django.urls import path
from app1 import views

urlpatterns = [
    path('ap/', views.myapp1, name='myapp1')
]