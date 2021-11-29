from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('gnc', views.dashboard, name='dashboard'),

]
