from django.contrib import admin
from django.urls import path
from app1.views import post_data, get_data

urlpatterns = [
    path('post/', post_data, name='post_data'),
    path('get/', get_data, name='get_data'),
]