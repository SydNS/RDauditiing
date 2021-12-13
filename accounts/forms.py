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


# class AccountsForm(forms.ModelForm):
#
#     class Meta:
#         model = GncTable
#         fields = "__all__"
#         widgets = {
#             'agreed_implementation_date': forms.DateInput(format=('%m/%d/%Y'),
#                                              attrs={'class': 'form-control', 'placeholder': 'Select a date',
#                                                     'type': 'date'}),
#             'revised_implementation_date': forms.DateInput(format=('%m/%d/%Y'),
#                                                           attrs={'class': 'form-control',
#                                                                  'placeholder': 'Select a date',
#                                                                  'type': 'date'}),
#             'actual_implementation_date': forms.DateInput(format=('%m/%d/%Y'),
#                                                           attrs={'class': 'form-control',
#                                                                  'placeholder': 'Select a date',
#                                                                  'type': 'date'}),
#         }
