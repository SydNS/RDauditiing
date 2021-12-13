from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    # path('', views.dashboard, name='dashboard'),
    # path('login/', views.loginuser, name='login'),
    # path('register/', views.Registering, name='register'),
    # path('logout/', views.Logout, name='logout'),
    #
    # Auditor of auditors
    path('a_o_apractices/', views.AuditorsPractices, name='a_o_apractices'),
    path('a_o_arecommendations/', views.AuditorsRecommendations, name='a_o_arecommendations'),
    path('a_o_aconsolidated/', views.AuditorsConsolidated, name='a_o_aconsolidated'),

]
