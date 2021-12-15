from django.contrib import admin
from django.urls import path, include
from . import views

app_name="governance_app"
urlpatterns = [

    path('', views.dashboard, name='dashboard'),

    # governance and governances
    path('governcontrolprojects/', views.Governcontrolprojects, name='governcontrolprojects'),
    path('governcontrolissues/', views.GoverncontrolIssues, name='governcontrolissues'),
    path('governcontrolrecommendations/', views.Governcontrolrecommendations, name='governcontrolrecommendations'),
    path('governcontrolconsolidated/', views.Governcontrolconsolidated, name='governcontrolconsolidated'),

    # governance and governances details
    path('governcontrolprojects/<int:id>/', views.GoverncontrolprojectsDetail, name='governcontrolprojectsdetails'),


    # Add governance and governances
    path('addgoverncontrol/', views.AddGoverncontrolprojects, name='addgoverncontrol'),





]
