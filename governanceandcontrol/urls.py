from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.dashboard, name='dashboard'),
    path('login/', views.loginuser, name='dashboard'),
    path('register/', views.Registering, name='register'),

]
