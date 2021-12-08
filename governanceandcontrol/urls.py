from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.dashboard, name='dashboard'),
    path('login/', views.loginuser, name='login'),
    path('register/', views.Registering, name='register'),
    path('logout/', views.Logout, name='logout'),
    path('auditprojects/', views.Auditprojects, name='auditprojects'),
    path('auditissues/', views.AuditIssues, name='auditissues'),
    path('governcontrol/', views.Governcontrol, name='governcontrol'),
    path('auditrecommendations/', views.Auditrecommendations, name='auditrecommendations'),

]
