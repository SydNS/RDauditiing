from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('login/', views.loginuser, name='login'),
    path('register/', views.Registering, name='register'),
    path('logout/', views.Logout, name='logout'),

    path("", include("governanceandcontrol.urls"),name="dashboard"),

]
