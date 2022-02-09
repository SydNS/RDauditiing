from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout  # add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import Person,RatingUser
# Create your views here.


def Registering(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("governance_app:dashboard")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="accounts/register.html", context={"register_form": form})


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
                return redirect("governance_app:dashboard")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="accounts/login.html", context={"login_form": form})
    # return render(request, , info)


def Logout(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')

def Employeesview(request):
    people=Person.objects.all()
    ratings=RatingUser.objects.all()
    return render(request=request, template_name="accounts/people.html", context={"people": people,"ratings": ratings,})


def Personview(request,id):
    person=Person.objects.get(id=id)
    xy=person.id
    rating=RatingUser.objects.get( person=xy)
    return render(request=request, template_name="accounts/person.html", context={"person": person,
                                                                                  "rating": rating,
                                                                                  })
