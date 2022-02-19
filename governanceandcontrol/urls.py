from django.contrib import admin
from django.urls import path, include
from . import views

app_name="governance_app"
urlpatterns = [

    path('', views.dashboard, name='dashboard'),

    # governance and governances
    path('governanceandcontrolprojects/', views.Governcontrolprojects, name='governcontrolprojects'),
    path('governanceandcontrolissues/', views.GoverncontrolIssues, name='governcontrolissues'),
    path('governanceandcontrolrecommendations/', views.Governcontrolrecommendations, name='governcontrolrecommendations'),
    path('governanceandcontrolconsolidated/', views.Governcontrolconsolidated, name='governcontrolconsolidated'),

    # governance and governances details
    path('governanceandcontrolprojects/<int:id>/', views.GoverncontrolprojectsDetail, name='governcontrolprojectsdetails'),

    # Add governance and governances
    path('addgovernanceandcontrol/', views.AddGoverncontrolprojects, name='addgoverncontrol'),
    path('editgovernanceandcontrol/<int:id>/', views.EditGoverncontrolprojects, name='editgoverncontrol'),


    # Frequently Asked Questions
    path('faq/', views.FAQ, name='faq'),





]
