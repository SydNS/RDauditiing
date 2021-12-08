from django.shortcuts import render
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout  # add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm  # add this


# Create your views here.
def dashboard(request):
    gncobj = models.GncTable.objects.all()
    # info =
    return render(request, 'governanceandcontrol/index.html', {
        "gncojbects": gncobj
    })


def loginuser(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("dashboard")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="governanceandcontrol/login.html", context={"login_form": form})
    # return render(request, , info)


def Registering(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("dashboard")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="governanceandcontrol/register.html", context={"register_form": form})


def Logout(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')

def Auditprojects(request):
    # if request.method == "POST":
    #     form = NewUserForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         login(request, user)
    #         messages.success(request, "Registration successful.")
    #         return redirect("dashboard")
    #     messages.error(request, "Unsuccessful registration. Invalid information.")
    # form = NewUserForm()
    return render(request=request, template_name="governanceandcontrol/auditprojects.html")


def AuditIssues(request):
    # if request.method == "POST":
    #     form = NewUserForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         login(request, user)
    #         messages.success(request, "Registration successful.")
    #         return redirect("dashboard")
    #     messages.error(request, "Unsuccessful registration. Invalid information.")
    # form = NewUserForm()
    return render(request=request, template_name="governanceandcontrol/auditissues.html")


