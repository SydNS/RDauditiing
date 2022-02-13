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
    return redirect('accounts:login')

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

# profile registering
# @login_required
def ProfileSetting(request):
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES)

        if profile_form.is_valid():
            try:
                student = profile_form.save(commit=True)
                student.save()
                print(student.photo)
                registered = True
                return HttpResponseRedirect("/profiledetails")
            except:
                messages.error(request, "Sorry something went worng.")
        # else:
        #     return HttpResponseRedirect('<p>Hello</p>')

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    elif request.method == 'GET':
        profile_form = ProfileForm(initial={'name_user': request.user})
        # profile_form.fields["name_user"]=request.user

    return render(request, 'dashboard/hostel/hostelstudentprofile.html', {
        'profile_form': profile_form,
        'registered': registered,
    })


def Profiledetails(request):
    currentuser = request.user
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES)

        # fetch the object related to passed user in the GET request
        profile_deatils_to_update = Student.objects.get(name_user=currentuser)

        # pass the object as instance in form
        profile_deatils_to_update_form = ProfileForm(request.POST,request.FILES, instance=profile_deatils_to_update)

        if profile_form.is_valid():
            try:
                student = profile_deatils_to_update_form.save(commit=True)
                student.save()
                registered = True
                return HttpResponseRedirect("/profiledetails")
            except:
                pass
        # else:
        #     return HttpResponseRedirect('<p>Hello</p>')

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    elif request.method == 'GET':
        # profile_deatils = Student.objects.get(name_user=request.user)

        # if not profile_deatils:
        #
        try:
            profile_deatils = Student.objects.get(name_user=request.user)
            profile_form = ProfileForm(initial={
                'name_user': profile_deatils.name_user,
                'photo': profile_deatils.photo,
                'gender': profile_deatils.gender,
                'date_of_birth': profile_deatils.date_of_birth,
                'reporting_date': profile_deatils.reporting_date,
                'address': profile_deatils.address,
                'parent_name': profile_deatils.parent_name,
                'phonenumber': profile_deatils.phonenumber,
                'city': profile_deatils.city,
                'state': profile_deatils.state,
                'studentIdnumber': profile_deatils.studentIdnumber,
                'level_of_study': profile_deatils.level_of_study

            })

            age = datetime.datetime.now()
            age = age.year
            age = age - profile_deatils.date_of_birth.year

            return render(request, 'dashboard/hostel/userprofiledetails.html', {
                'profile_deatils': profile_deatils,
                'profile_form': profile_form,
                'mod_profile': "Edit Profile",
                'age': age
            })

        except:
            profile_deatils = {
                'name_user': "Enter Your Name Here",
                'gender': "Gender",
                'date_of_birth': "Enter Birthday",
                'reporting_date': "Reporting Date",
                'address': "Your Address",
                'parent_name': "Parent Names",
                'phonenumber': "Phone Contact",
                'city': "Home City",
                'state': "State/Region",
                'studentIdnumber': "Your ID.Numebr",
                'level_of_study': "Year Of Study"

            }
            profile_form = ProfileForm(initial={
                'name_user': "Enter Your Name ",
                'gender': "Gender",
                'date_of_birth': "Enter Birthday",
                'reporting_date': "Reporting Date",
                'address': "Your Address",
                'parent_name': "Parent Names",
                'phonenumber': "Phone Contact",
                'city': "Home City",
                'state': "State/Region",
                'studentIdnumber': "Your ID.Numebr",
                'level_of_study': "Year Of Study"

            })
            age = datetime.datetime.now()
            age = age.year
            age = age - 2003
            req_age = "Should be atleast" + str(age)
            return render(request, 'dashboard/hostel/userprofiledetails.html', {
                'profile_deatils': profile_deatils,
                'profile_form': profile_form,
                'mod_profile': "Create Profile",
                'age': req_age
            })


def Customersview(request):
    profile_deatils = Student.objects.all()
    totalusers = profile_deatils.count()

    return render(request, 'dashboard/hostel/studentslistwithimages.html', {
        'profile_deatils': profile_deatils,
        'totalusers': totalusers,

    })

def Customerdetailsview(request,id):
    profile_deatils = Student.objects.get(id=id)

    return render(request, 'dashboard/hostel/userprofiledetails.html', {
        'profile_deatils': profile_deatils,

    })