from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

# Create your forms here.
from .models import GncTable


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class GncTableForm(forms.Form):
    class Meta:
        model = GncTable
        fields = ['audit_project_code', 'audit_project_name', 'quarter', 'audit_project_type',
                  'issue_title', 'criticality', 'root_cause_analysis', 'recommendation',
                  'action_plan', 'recommendation_state', 'agreed_implementation_date', 'revised_implementation_date'
            , 'last_status_update', 'ageing_days', 'actual_implementation_date', 'owner', 'final_approver',
                  ]
