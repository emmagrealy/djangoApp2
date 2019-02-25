from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import redirect

def index(request):
    return render(request, 'home/index.html')

def login(request):
    print(request.POST)
    username = request.POST.get("Username")
    password = request.POST.get("Password")
    return render(request, 'home/profile.html', {'Username': username, 'Password': password})

def signUpForm(request):
    return render(request, 'home/signUpForm.html')

def signUp(request):
    print(request.POST)
    username = request.POST.get("Username")
    password = request.POST.get("Password")
    email = request.POST.get("Email")
    return render(request, 'home/profile.html', {'Username': username, 'Password': password, 'Email': email})
