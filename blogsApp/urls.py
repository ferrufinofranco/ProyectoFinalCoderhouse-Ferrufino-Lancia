from django.urls import path
from blogsApp.views import *

urlpatterns = [
    path('home/', home, name='Inicio'),
]