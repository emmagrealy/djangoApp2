from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    # log in success leads to this page
    path('login/', views.login, name='login'),

    #sign up button leads here
    path('signUpForm/', views.signUpForm, name='signUpForm'),
    
    #sign up form leads here
    path('signUp/', views.signUp, name='signUp')
]