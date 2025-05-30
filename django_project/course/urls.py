from django.urls import path
from course.views import learn_django, learn_fastAPI

urlpatterns = [
    path('dj/', learn_django),
    path('fst/', learn_fastAPI),
]