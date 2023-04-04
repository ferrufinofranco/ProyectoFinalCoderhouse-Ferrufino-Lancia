from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from blogsApp.models import *
from blogsApp.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

def home(request):
    return render(request, "base/base.html")
