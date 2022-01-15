from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [



    # risk management
    path('risks/', views.Risks, name='risks'),
    path('riskcontrol/', views.RiskControl, name='riskcontrol'),
    path('keyrateindicator/', views.KRI, name='keyrateindicator'),

    # Risks details
    path('risks/<int:id>/', views.RisksDetail, name='risksdetails'),

    # addrisk
    path('addrisk/', views.AddRiskRecords, name='addrisk'),



]
