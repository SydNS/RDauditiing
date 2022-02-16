from django.contrib import admin
from django.urls import path, include
from . import views
from .apps import AccountsConfig

app_name='accounts'
urlpatterns = [

    path('login/', views.loginuser, name='login'),
    path('register/', views.registering, name='register'),

    path('profilesetup/', views.profileSetting, name='profilesetup'),
    path('profilesetup/<int:id>/', views.profileEditing, name='profileediting'),

    path('profiledetails/', views.profiledetails, name='profiledetails'),

    path('logout/', views.logout, name='logout'),

    # peopleview
    path('employees/', views.employeesview, name='employees'),
    path('accountshome/', views.accountshome, name='accountshome'),
    path('employee/<int:id>/', views.personview, name='employee'),

    path("", include("governanceandcontrol.urls"),name="dashboard"),

]
