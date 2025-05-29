"""
URL configuration for djangoAPIs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

"""from app1 import views as ap1
from app2 import views as ap2"""

from app1.views import myfun1, myfun2
from app2.views import myfun1, myfun2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myfun1, name='myfun1'),
    path('hi/', myfun2, name='myfun2'),

    path('', myfun1, name='myfun1'),
    path('di/', myfun2, name='myfun2'),

]
