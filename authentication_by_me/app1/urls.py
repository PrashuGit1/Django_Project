from django.urls import path
from app1.views import home, login, dashboard
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='app1/login.html'), name='login'),
    path('',home,name='name'),
    path('/dashboard',dashboard,name='dashboard'),
]