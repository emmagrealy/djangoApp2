from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect , reverse
from django.http import HttpResponseRedirect
from django.contrib import messages


def index(request):
    return render(request, 'home/index.html')

def signIn(request):
    print(request.POST)
    username = request.POST.get("Username")
    password = request.POST.get("Password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('home:profile'))
    else:
        messages.add_message(request, messages.INFO, 'Invalid LogIn Details!')
        return render(request, 'home/index.html')
        


def signUpForm(request):
    return render(request, 'home/signUpForm.html')


def signUp(request):
    print(request.POST)
    username = request.POST.get("Username")
    password = request.POST.get("Password")
    email = request.POST.get("Email")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
          user = User.objects.create_user(username, password, email)
          user.save()
          login(request, user)

    return HttpResponseRedirect(reverse('home:profile'))


def profile(request):
    return render(request, 'home/profile.html')