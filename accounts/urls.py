from django.contrib import admin
from django.urls import path, include
from . import views
from .apps import AccountsConfig

app_name='accounts'
urlpatterns = [

    path('login/', views.loginuser, name='login'),
    path('register/', views.Registering, name='register'),
    path('logout/', views.Logout, name='logout'),

    # peopleview
    path('employees/', views.Employeesview, name='employees'),

    path("", include("governanceandcontrol.urls"),name="dashboard"),

]
