import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm, ProfileForm
from django.contrib.auth import login, authenticate, logout  # add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from . import models
from governanceandcontrol.models import Governance_And_Control
from riskmanagement.models import RiskManagement
from auditor_of_auditors.models import Auditor_of_auditors
from accounts.models import Department
from accounts.models import Person
from accounts.models import RatingUser


# Create your views here.


def registering(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("accounts:profilesetup")
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


def logout(request):
    messages.info(request, "You have successfully logged out.")
    return redirect('accounts:login')


def employeesview(request):
    people = models.Person.objects.all()
    try:
        ratings = models.RatingUser.objects.all()
    except:
        ratings = {}
    return render(request=request, template_name="accounts/people.html",
                  context={"people": people, "ratings": ratings, })


def personview(request, id):
    try:
        person = models.Person.objects.get(id=id)
        try:
            people_in_same_dept = models.Person.objects.filter(personsdept=models.Person.objects.get(id=id).personsdept)
            print(people_in_same_dept)
            people_in_same_address = models.Person.objects.filter(address=models.Person.objects.get(id=id).address)
            print(people_in_same_address)
            print("==============================")
            length_username_in_request = len(str(request.user))
            length_username_in_person_obj = len(str(person.name_user))
            if len(str(person.name_user)) == len(str(request.user)):
                print(yes)

            rating = models.RatingUser.objects.get(person=person.id)

            rating_range = range(rating.rate_level)
            rating_reverse_range = range(10 - rating.rate_level)
        except:
            rating = 1
            rating_range = range(1)
            rating_reverse_range = range(10 - 1)
        return render(request=request, template_name="accounts/person.html", context={"person": person,
                                                                                      "rating": rating,
                                                                                      "rating_range": rating_range,
                                                                                      "rating_reverse_range": rating_reverse_range,
                                                                                      "people_in_same_dept": people_in_same_dept,
                                                                                      "people_in_same_address": people_in_same_address,
                                                                                      # permitting
                                                                                      "length_username_in_request": length_username_in_request,
                                                                                      "length_username_in_person_obj": length_username_in_person_obj,
                                                                                      })
    except:
        return redirect('accounts:profileediting', id)


# profile registering
# @login_required
def profileSetting(request):
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES)

        if profile_form.is_valid():
            try:
                person = profile_form.save(commit=True)
                person.save()
                print(Person.photo)
                registered = True
                return redirect("accounts:profiledetails")
            except:
                print("Person.photo")
                messages.error(request, "Sorry something went worng.")
        # else:
        #     return HttpResponseRedirect('<p>Hello</p>')

    profile_form = ProfileForm(initial={'name_user': request.user})
    # profile_form.fields["name_user"]=request.user

    return render(request, 'accounts/profilesetup.html', {
        'form': profile_form,
    })


# @login_required
def profileEditing(request, id):
    try:
        personEdit = models.Person.objects.get(id=id)
        people_in_same_dept = models.Person.objects.filter(personsdept=models.Person.objects.get(id=id).personsdept)
        print(people_in_same_dept)
        people_in_same_address = models.Person.objects.filter(address=models.Person.objects.get(id=id).address)
        print(people_in_same_address)
        person = models.Person.objects.get(id=id)
        rating = models.RatingUser.objects.get(person=person.id)
        rating_range = range(rating.rate_level)
        rating_reverse_range = range(10 - rating.rate_level)
        if request.method == 'POST':
            profile_form = ProfileForm(request.POST, request.FILES)

            if profile_form.is_valid():
                try:
                    person = profile_form.save(commit=True)
                    person.save()
                    print(Person.photo)
                    registered = True
                    return redirect("accounts:profiledetails")
                except:
                    print("Person.photo")
                    messages.error(request, "Sorry something went worng.")
            # else:
            #     return HttpResponseRedirect('<p>Hello</p>')

        profile_form = ProfileForm(instance=personEdit)
        # profile_form.fields["name_user"]=request.user

        return render(request, 'accounts/edit_person.html', {
            'form': profile_form,
            "person": person,
            "rating": rating,
            "rating_range": rating_range,
            "rating_reverse_range": rating_reverse_range,
            "people_in_same_dept": people_in_same_dept,
            "people_in_same_address": people_in_same_address,
        })
    except:
        profile_form = ProfileForm(
            initial={'name_user': request.user, 'last_name': 'Last Name', 'first_name': 'First Name', 'photo': '', })
        return render(request, 'accounts/edit_person.html', {
            'form': profile_form,
        })


def profiledetails(request):
    currentuser = request.user
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES)

        # fetch the object related to passed user in the GET request
        profile_deatils_to_update = models.Person.objects.get(name_user=currentuser)

        # pass the object as instance in form
        profile_deatils_to_update_form = ProfileForm(request.POST, request.FILES, instance=profile_deatils_to_update)

        if profile_form.is_valid():
            try:
                Person = profile_deatils_to_update_form.save(commit=True)
                Person.save()
                registered = True
                return redirect("profiledetails")
            except:
                pass
    elif request.method == 'GET':
        try:
            profile_deatils = models.Person.objects.get(name_user=request.user)
            profile_form = ProfileForm(initial=profile_deatils)
            print(profile_deatils)

            return render(request, 'accounts/person.html', {
                'person': profile_deatils,
                'profile_form': profile_form,
                'mod_profile': "Edit Profile",
                'age': age
            })

        except:
            profile_deatils = models.Person.objects.get(name_user=request.user)
            print(profile_deatils, profile_deatils.name_user, profile_deatils.last_name, profile_deatils.first_name,
                  profile_deatils.photo, )
            # profile_form = ProfileForm(initial=profile_deatils)
            return render(request, 'accounts/person.html', {
                'person': profile_deatils,
                # 'profile_form': profile_form,
                'mod_profile': "Create Profile",
            })


# noinspection PyUnresolvedReferences
def accountshome(request):
    people = models.Person.objects.all().exclude(name_user=request.user)
    if not people:
        person = {}
        ratings = {}
        labels = []
        data = []
        for rate in ratings:
            labels.append(rate.person)
            data.append(rate.rate_level)
        return render(request, 'accounts/accounts_home.html',
                      {'label': labels, 'ratings': data, 'rating_range': range(4),
                       'people': people, 'person': person, })
    else:
        person = models.Person.objects.get(name_user=request.user)
        ratings = models.RatingUser.objects.all().order_by('-rate_level')[:5]
        labels = []
        data = []
        for rate in ratings:
            labels.append(rate.person)
            data.append(rate.rate_level)
        return render(request, 'accounts/accounts_home.html',
                      {'label': labels, 'ratings': data, 'rating_range': range(4),
                       'people': people, 'person': person, })

