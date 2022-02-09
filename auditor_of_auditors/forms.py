from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

# Create your forms here.
from .models import Auditor_of_auditors

class Auditor_of_auditorsForm(forms.ModelForm):

    class Meta:
        model = Auditor_of_auditors
        fields = "__all__"
        widgets = {
            'agreed_implementation_date': forms.DateInput(format=('%m/%d/%Y'),
                                             attrs={'class': 'form-control', 'placeholder': 'Select a date',
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
