from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.



def Registering():
    formreg=UserCreationForm()
    return render(request,'',{'form':formreg})