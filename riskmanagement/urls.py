from django.contrib import admin
from django.urls import path, include
from . import views
from .apps import RiskmanagementConfig

app_name=RiskmanagementConfig.name
urlpatterns = [

    # risk management
    path('risks/', views.Risks, name='risks'),
    path('risks_consolidated/', views.Risks_consolidated, name='risks_consolidated'),
    path('riskcontrol/', views.RiskControl, name='riskcontrol'),
    path('keyrateindicator/', views.KRI, name='keyrateindicator'),

    # Risks details
    path('risk/<int:id>/', views.RisksDetail, name='risksdetails'),

    # addrisk
    path('addrisk/', views.AddRiskRecords, name='addrisk'),

    # editrisk
    path('editrisk/<int:id>/', views.EditRiskRecords, name='editrisk'),



]
