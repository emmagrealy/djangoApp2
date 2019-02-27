from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    # log in success leads to this page
    path('signIn/', views.signIn, name='signIn'),

    #sign up button leads here
    path('signUpForm/', views.signUpForm, name='signUpForm'),
    
    #sign up form leads here
    path('signUp/', views.signUp, name='signUp')
]