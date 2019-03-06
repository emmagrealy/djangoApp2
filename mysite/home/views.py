from django.shortcuts import render
from django.contrib.auth.models import User  
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Post
from django.contrib.auth import logout
from django.template import loader

#index
def index(request):
    return render(request, 'home/index.html')

#sign in
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
        return HttpResponseRedirect(reverse('home:index'))

#sign up form  
def signUpForm(request):
    return render(request, 'home/signUpForm.html')

#sign up
def signUp(request):
    print(request.POST)
    username = request.POST.get("Username")
    password = request.POST.get("Password")
    email = request.POST.get("Email")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
          user = User.objects.create_user(username, email, password)
          user.save()
          login(request, user)

    return HttpResponseRedirect(reverse('home:profile'))

#profile
def profile(request):
    return render(request, 'home/profile.html')

#make post
def makePost(request):
    print(request.POST)
    title = request.POST.get("Title")
    description = request.POST.get("Description")
    myfile = request.FILES['image']
    post = Post.objects.create(title=title, description=description, image=myfile)
    post.save()
    return HttpResponseRedirect(reverse('home:postFeed'))


def postFeed(request):

    latest_post_list = Post.objects.order_by('id')

    context = {
        'latest_post_list': latest_post_list,
    }
    return render(request, 'home/postFeed.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home:index'))

def viewPost(request, pk):
    post = post.objects.get(pk = pk)
    contect = {'post':post}
    print(request.POST)
    return render(request, 'home/viewPost.html', context)
