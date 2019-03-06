from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    # log in success leads to this page
    path('signIn/', views.signIn, name='signIn'),

    #sign up button leads here
    path('signUpForm/', views.signUpForm, name='signUpForm'),
    
    #sign up form leads here
    path('signUp/', views.signUp, name='signUp'),

    #profile
    path('profile/', views.profile, name='profile'),

    #post to profile
    path('profile/', views.makePost, name='makePost'),

    #make a post
    path('makePost/', views.makePost, name='makePost'),

    #post feed
    path('postFeed/', views.postFeed, name='postFeed'),

    #logout
    path('logout_view/', views.logout_view, name='logout_view'),

    #specific post
    path('viewPost/<pk>/', views.viewPost, name='viewPost'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)