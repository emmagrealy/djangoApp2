from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect , reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django import forms


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
        return HttpResponseRedirect(reverse('home/profile.html'))
    else:
        messages.add_message(request, messages.INFO, 'Invalid LogIn Details!')
        return HttpResponseRedirect(reverse, 'home/index.html')

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
          user = User.objects.create_user(username, password, email)
          user.save()
          login(request, user)

    return HttpResponseRedirect(reverse('home:profile'))

#profile
def profile(request):
    return render(request, 'home/profile.html')

#make post
def makePost(request):
   def makePost(request):
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail')
    else:
        form = makePost(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})