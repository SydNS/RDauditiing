from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

# Create your forms here.
from .models import RiskManagement

class RiskManagementForm(forms.ModelForm):

    class Meta:
        model = RiskManagement
        fields = "__all__"
        widgets = {
            'likelihood': forms.RadioSelect(attrs={'class': 'form-control', 'placeholder': 'Chances of occuring',
                                                    'type': 'date'}),
            'revised_implementation_date': forms.DateInput(format=('%m/%d/%Y'),
                                                          attrs={'class': 'form-control',
                                                                 'placeholder': 'Select a date',
                                                                 'type': 'date'}),
            'actual_implementation_date': forms.DateInput(format=('%m/%d/%Y'),
                                                          attrs={'class': 'form-control',
                                                                 'placeholder': 'Select a date',
                                                                 'type': 'date'}),
        }
