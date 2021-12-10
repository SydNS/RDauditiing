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


def Governcontrolprojects(request):
    consolidatedgncobj = models.GncTable.objects.all()
    consolidatedgncobjnumber = models.GncTable.objects.all().count()
    #
    # CRITICAL_LEVELS = (
    #     ('low', 'low'),
    #     ('medium', 'medium'),
    #     ('high', 'high'),
    # )
    # QUARTERS = (
    #     ('Q1', 'Q1'),
    #     ('Q2', 'Q2'),
    #     ('Q3', 'Q3'),
    #     ('Q4', 'Q4'),
    # )
    # ROOT_CAUSE_ANALYSIS = (
    #     ('POCESSES', 'POCESSES'),
    #     ('PEOPLE', 'PEOPLE'),
    #     ('TECHNOLOGY', 'TECHNOLOGY'),
    # )

    # counting the number issues at different levels of criticality
    mediumimpactissues = models.GncTable.objects.filter(
        criticality='medium',
    ).count()
    highimpactissues = models.GncTable.objects.filter(
        criticality='high',
    ).count()
    lowimpactissues = models.GncTable.objects.filter(
        criticality='low',
    ).count()

    # counting the number issues at different levels of state
    # RECOMMENDATION_STATE = (
    #     ('PARTIALLY_IMPLEMENTED', 'PARTIALLY_IMPLEMENTED'),
    #     ('PENDING', 'PENDING'),
    #     ('CLOSED', 'CLOSED'),
    # )
    PENDING = models.GncTable.objects.filter(
        recommendation_state='PENDING',
    ).count()
    CLOSED = models.GncTable.objects.filter(
        recommendation_state='CLOSED',
    ).count()
    PARTIALLY_IMPLEMENTED = models.GncTable.objects.filter(
        recommendation_state='PARTIALLY_IMPLEMENTED',
    ).count()
    # percentage of completed recos
    percentagecompleted = round((CLOSED / consolidatedgncobjnumber) * 100, 1)

    # ageing days total

    for totaldays in consolidatedgncobj:
        totaldays = +totaldays.ageing_days

    return render(request=request, template_name="governanceandcontrol/governcontrolprojects.html",
                  context={
                      "consolidateddata": consolidatedgncobj,
                      "consolidatedgncobjnumber": consolidatedgncobjnumber,

                      # issues
                      "mediumimpactissues": mediumimpactissues,
                      "highimpactissues": highimpactissues,
                      "lowimpactissues": lowimpactissues,

                      # reommendations
                      "PARTIALLY_IMPLEMENTED": PARTIALLY_IMPLEMENTED,
                      "PENDING": PENDING,
                      "CLOSED": CLOSED,
                      "percentagecompleted": percentagecompleted,

                      # reommendations
                      "totaldays": round(totaldays, 1),

                  }
                  )


def GoverncontrolIssues(request):
    consolidatedgncobj = models.GncTable.objects.all()
    consolidatedgncobjnumber = models.GncTable.objects.all().count()
    #
    # CRITICAL_LEVELS = (
    #     ('low', 'low'),
    #     ('medium', 'medium'),
    #     ('high', 'high'),
    # )
    # QUARTERS = (
    #     ('Q1', 'Q1'),
    #     ('Q2', 'Q2'),
    #     ('Q3', 'Q3'),
    #     ('Q4', 'Q4'),
    # )
    # ROOT_CAUSE_ANALYSIS = (
    #     ('POCESSES', 'POCESSES'),
    #     ('PEOPLE', 'PEOPLE'),
    #     ('TECHNOLOGY', 'TECHNOLOGY'),
    # )

    # counting the number issues at different levels of criticality
    mediumimpactissues = models.GncTable.objects.filter(
        criticality='medium',
    ).count()
    highimpactissues = models.GncTable.objects.filter(
        criticality='high',
    ).count()
    lowimpactissues = models.GncTable.objects.filter(
        criticality='low',
    ).count()

    # counting the number issues at different levels of state
    # RECOMMENDATION_STATE = (
    #     ('PARTIALLY_IMPLEMENTED', 'PARTIALLY_IMPLEMENTED'),
    #     ('PENDING', 'PENDING'),
    #     ('CLOSED', 'CLOSED'),
    # )
    PENDING = models.GncTable.objects.filter(
        recommendation_state='PENDING',
    ).count()
    CLOSED = models.GncTable.objects.filter(
        recommendation_state='CLOSED',
    ).count()
    PARTIALLY_IMPLEMENTED = models.GncTable.objects.filter(
        recommendation_state='PARTIALLY_IMPLEMENTED',
    ).count()
    # percentage of completed recos
    percentagecompleted = round((CLOSED / consolidatedgncobjnumber) * 100, 1)

    # ageing days total

    for totaldays in consolidatedgncobj:
        totaldays = +totaldays.ageing_days

    return render(request=request, template_name="governanceandcontrol/governcontrolissues.html",
                  context={
                      "consolidateddata": consolidatedgncobj,
                      "consolidatedgncobjnumber": consolidatedgncobjnumber,

                      # issues
                      "mediumimpactissues": mediumimpactissues,
                      "highimpactissues": highimpactissues,
                      "lowimpactissues": lowimpactissues,

                      # reommendations
                      "PARTIALLY_IMPLEMENTED": PARTIALLY_IMPLEMENTED,
                      "PENDING": PENDING,
                      "CLOSED": CLOSED,
                      "percentagecompleted": percentagecompleted,

                      # reommendations
                      "totaldays": round(totaldays, 1),

                  })


def Governcontrolrecommendations(request):
    consolidatedgncobj = models.GncTable.objects.all()
    consolidatedgncobjnumber = models.GncTable.objects.all().count()
    #
    # CRITICAL_LEVELS = (
    #     ('low', 'low'),
    #     ('medium', 'medium'),
    #     ('high', 'high'),
    # )
    # QUARTERS = (
    #     ('Q1', 'Q1'),
    #     ('Q2', 'Q2'),
    #     ('Q3', 'Q3'),
    #     ('Q4', 'Q4'),
    # )
    # ROOT_CAUSE_ANALYSIS = (
    #     ('POCESSES', 'POCESSES'),
    #     ('PEOPLE', 'PEOPLE'),
    #     ('TECHNOLOGY', 'TECHNOLOGY'),
    # )

    # counting the number issues at different levels of criticality
    mediumimpactissues = models.GncTable.objects.filter(
        criticality='medium',
    ).count()
    highimpactissues = models.GncTable.objects.filter(
        criticality='high',
    ).count()
    lowimpactissues = models.GncTable.objects.filter(
        criticality='low',
    ).count()

    # counting the number issues at different levels of state
    # RECOMMENDATION_STATE = (
    #     ('PARTIALLY_IMPLEMENTED', 'PARTIALLY_IMPLEMENTED'),
    #     ('PENDING', 'PENDING'),
    #     ('CLOSED', 'CLOSED'),
    # )
    PENDING = models.GncTable.objects.filter(
        recommendation_state='PENDING',
    ).count()
    CLOSED = models.GncTable.objects.filter(
        recommendation_state='CLOSED',
    ).count()
    PARTIALLY_IMPLEMENTED = models.GncTable.objects.filter(
        recommendation_state='PARTIALLY_IMPLEMENTED',
    ).count()
    # percentage of completed recos
    percentagecompleted = round((CLOSED / consolidatedgncobjnumber) * 100, 1)

    # ageing days total

    for totaldays in consolidatedgncobj:
        totaldays = +totaldays.ageing_days

    return render(request=request, template_name="governanceandcontrol/auditrecommendations.html",
                  context={
                      "consolidateddata": consolidatedgncobj,
                      "consolidatedgncobjnumber": consolidatedgncobjnumber,

                      # issues
                      "mediumimpactissues": mediumimpactissues,
                      "highimpactissues": highimpactissues,
                      "lowimpactissues": lowimpactissues,

                      # reommendations
                      "PARTIALLY_IMPLEMENTED": PARTIALLY_IMPLEMENTED,
                      "PENDING": PENDING,
                      "CLOSED": CLOSED,
                      "percentagecompleted": percentagecompleted,

                      # reommendations
                      "totaldays": round(totaldays, 1),

                  })


def Governcontrolconsolidated(request):
    consolidatedgncobj = models.GncTable.objects.all()
    consolidatedgncobjnumber = models.GncTable.objects.all().count()
    #
    # CRITICAL_LEVELS = (
    #     ('low', 'low'),
    #     ('medium', 'medium'),
    #     ('high', 'high'),
    # )
    # QUARTERS = (
    #     ('Q1', 'Q1'),
    #     ('Q2', 'Q2'),
    #     ('Q3', 'Q3'),
    #     ('Q4', 'Q4'),
    # )
    # ROOT_CAUSE_ANALYSIS = (
    #     ('POCESSES', 'POCESSES'),
    #     ('PEOPLE', 'PEOPLE'),
    #     ('TECHNOLOGY', 'TECHNOLOGY'),
    # )

    # counting the number issues at different levels of criticality
    mediumimpactissues = models.GncTable.objects.filter(
        criticality='medium',
    ).count()
    highimpactissues = models.GncTable.objects.filter(
        criticality='high',
    ).count()
    lowimpactissues = models.GncTable.objects.filter(
        criticality='low',
    ).count()

    # counting the number issues at different levels of state
    # RECOMMENDATION_STATE = (
    #     ('PARTIALLY_IMPLEMENTED', 'PARTIALLY_IMPLEMENTED'),
    #     ('PENDING', 'PENDING'),
    #     ('CLOSED', 'CLOSED'),
    # )
    PENDING = models.GncTable.objects.filter(
        recommendation_state='PENDING',
    ).count()
    CLOSED = models.GncTable.objects.filter(
        recommendation_state='CLOSED',
    ).count()
    PARTIALLY_IMPLEMENTED = models.GncTable.objects.filter(
        recommendation_state='PARTIALLY_IMPLEMENTED',
    ).count()
    # percentage of completed recos
    percentagecompleted = round((CLOSED / consolidatedgncobjnumber) * 100, 1)

    # ageing days total

    for totaldays in consolidatedgncobj:
        totaldays = +totaldays.ageing_days

    return render(request=request, template_name="governanceandcontrol/governcontrolconsolidated.html",
                  context={
                      "consolidateddata": consolidatedgncobj,
                      "consolidatedgncobjnumber": consolidatedgncobjnumber,

                      # issues
                      "mediumimpactissues": mediumimpactissues,
                      "highimpactissues": highimpactissues,
                      "lowimpactissues": lowimpactissues,

                      # reommendations
                      "PARTIALLY_IMPLEMENTED": PARTIALLY_IMPLEMENTED,
                      "PENDING": PENDING,
                      "CLOSED": CLOSED,
                      "percentagecompleted": percentagecompleted,

                      # reommendations
                      "totaldays": round(totaldays, 1),

                  })


# Risk management section
def Risks(request):
    consolidatedgncobj = models.GncTable.objects.all()
    consolidatedgncobjnumber = models.GncTable.objects.all().count()
    #
    # CRITICAL_LEVELS = (
    #     ('low', 'low'),
    #     ('medium', 'medium'),
    #     ('high', 'high'),
    # )
    # QUARTERS = (
    #     ('Q1', 'Q1'),
    #     ('Q2', 'Q2'),
    #     ('Q3', 'Q3'),
    #     ('Q4', 'Q4'),
    # )
    # ROOT_CAUSE_ANALYSIS = (
    #     ('POCESSES', 'POCESSES'),
    #     ('PEOPLE', 'PEOPLE'),
    #     ('TECHNOLOGY', 'TECHNOLOGY'),
    # )

    # counting the number issues at different levels of criticality
    mediumimpactissues = models.GncTable.objects.filter(
        criticality='medium',
    ).count()
    highimpactissues = models.GncTable.objects.filter(
        criticality='high',
    ).count()
    lowimpactissues = models.GncTable.objects.filter(
        criticality='low',
    ).count()

    # counting the number issues at different levels of state
    # RECOMMENDATION_STATE = (
    #     ('PARTIALLY_IMPLEMENTED', 'PARTIALLY_IMPLEMENTED'),
    #     ('PENDING', 'PENDING'),
    #     ('CLOSED', 'CLOSED'),
    # )
    PENDING = models.GncTable.objects.filter(
        recommendation_state='PENDING',
    ).count()
    CLOSED = models.GncTable.objects.filter(
        recommendation_state='CLOSED',
    ).count()
    PARTIALLY_IMPLEMENTED = models.GncTable.objects.filter(
        recommendation_state='PARTIALLY_IMPLEMENTED',
    ).count()
    # percentage of completed recos
    percentagecompleted = round((CLOSED / consolidatedgncobjnumber) * 100, 1)

    # ageing days total

    for totaldays in consolidatedgncobj:
        totaldays = +totaldays.ageing_days

    return render(request=request, template_name="governanceandcontrol/risks.html",
                  context={
                      "consolidateddata": consolidatedgncobj,
                      "consolidatedgncobjnumber": consolidatedgncobjnumber,

                      # issues
                      "mediumimpactissues": mediumimpactissues,
                      "highimpactissues": highimpactissues,
                      "lowimpactissues": lowimpactissues,

                      # reommendations
                      "PARTIALLY_IMPLEMENTED": PARTIALLY_IMPLEMENTED,
                      "PENDING": PENDING,
                      "CLOSED": CLOSED,
                      "percentagecompleted": percentagecompleted,

                      # reommendations
                      "totaldays": round(totaldays, 1),

                  })


# Risk management section
def RiskControl(request):
    consolidatedgncobj = models.GncTable.objects.all()
    consolidatedgncobjnumber = models.GncTable.objects.all().count()
    #
    # CRITICAL_LEVELS = (
    #     ('low', 'low'),
    #     ('medium', 'medium'),
    #     ('high', 'high'),
    # )
    # QUARTERS = (
    #     ('Q1', 'Q1'),
    #     ('Q2', 'Q2'),
    #     ('Q3', 'Q3'),
    #     ('Q4', 'Q4'),
    # )
    # ROOT_CAUSE_ANALYSIS = (
    #     ('POCESSES', 'POCESSES'),
    #     ('PEOPLE', 'PEOPLE'),
    #     ('TECHNOLOGY', 'TECHNOLOGY'),
    # )

    # counting the number issues at different levels of criticality
    mediumimpactissues = models.GncTable.objects.filter(
        criticality='medium',
    ).count()
    highimpactissues = models.GncTable.objects.filter(
        criticality='high',
    ).count()
    lowimpactissues = models.GncTable.objects.filter(
        criticality='low',
    ).count()

    # counting the number issues at different levels of state
    # RECOMMENDATION_STATE = (
    #     ('PARTIALLY_IMPLEMENTED', 'PARTIALLY_IMPLEMENTED'),
    #     ('PENDING', 'PENDING'),
    #     ('CLOSED', 'CLOSED'),
    # )
    PENDING = models.GncTable.objects.filter(
        recommendation_state='PENDING',
    ).count()
    CLOSED = models.GncTable.objects.filter(
        recommendation_state='CLOSED',
    ).count()
    PARTIALLY_IMPLEMENTED = models.GncTable.objects.filter(
        recommendation_state='PARTIALLY_IMPLEMENTED',
    ).count()
    # percentage of completed recos
    percentagecompleted = round((CLOSED / consolidatedgncobjnumber) * 100, 1)

    # ageing days total

    for totaldays in consolidatedgncobj:
        totaldays = +totaldays.ageing_days

    return render(request=request, template_name="governanceandcontrol/riskcontrol.html",
                  context={
                      "consolidateddata": consolidatedgncobj,
                      "consolidatedgncobjnumber": consolidatedgncobjnumber,

                      # issues
                      "mediumimpactissues": mediumimpactissues,
                      "highimpactissues": highimpactissues,
                      "lowimpactissues": lowimpactissues,

                      # reommendations
                      "PARTIALLY_IMPLEMENTED": PARTIALLY_IMPLEMENTED,
                      "PENDING": PENDING,
                      "CLOSED": CLOSED,
                      "percentagecompleted": percentagecompleted,

                      # reommendations
                      "totaldays": round(totaldays, 1),

                  })


# Risk management section
def KRI(request):
    consolidatedgncobj = models.GncTable.objects.all()
    consolidatedgncobjnumber = models.GncTable.objects.all().count()
    #
    # CRITICAL_LEVELS = (
    #     ('low', 'low'),
    #     ('medium', 'medium'),
    #     ('high', 'high'),
    # )
    # QUARTERS = (
    #     ('Q1', 'Q1'),
    #     ('Q2', 'Q2'),
    #     ('Q3', 'Q3'),
    #     ('Q4', 'Q4'),
    # )
    # ROOT_CAUSE_ANALYSIS = (
    #     ('POCESSES', 'POCESSES'),
    #     ('PEOPLE', 'PEOPLE'),
    #     ('TECHNOLOGY', 'TECHNOLOGY'),
    # )

    # counting the number issues at different levels of criticality
    mediumimpactissues = models.GncTable.objects.filter(
        criticality='medium',
    ).count()
    highimpactissues = models.GncTable.objects.filter(
        criticality='high',
    ).count()
    lowimpactissues = models.GncTable.objects.filter(
        criticality='low',
    ).count()

    # counting the number issues at different levels of state
    # RECOMMENDATION_STATE = (
    #     ('PARTIALLY_IMPLEMENTED', 'PARTIALLY_IMPLEMENTED'),
    #     ('PENDING', 'PENDING'),
    #     ('CLOSED', 'CLOSED'),
    # )
    PENDING = models.GncTable.objects.filter(
        recommendation_state='PENDING',
    ).count()
    CLOSED = models.GncTable.objects.filter(
        recommendation_state='CLOSED',
    ).count()
    PARTIALLY_IMPLEMENTED = models.GncTable.objects.filter(
        recommendation_state='PARTIALLY_IMPLEMENTED',
    ).count()
    # percentage of completed recos
    percentagecompleted = round((CLOSED / consolidatedgncobjnumber) * 100, 1)

    # ageing days total

    for totaldays in consolidatedgncobj:
        totaldays = +totaldays.ageing_days

    return render(request=request, template_name="governanceandcontrol/riskkri.html",
                  context={
                      "consolidateddata": consolidatedgncobj,
                      "consolidatedgncobjnumber": consolidatedgncobjnumber,

                      # issues
                      "mediumimpactissues": mediumimpactissues,
                      "highimpactissues": highimpactissues,
                      "lowimpactissues": lowimpactissues,

                      # reommendations
                      "PARTIALLY_IMPLEMENTED": PARTIALLY_IMPLEMENTED,
                      "PENDING": PENDING,
                      "CLOSED": CLOSED,
                      "percentagecompleted": percentagecompleted,

                      # reommendations
                      "totaldays": round(totaldays, 1),

                  })


# ====================================== Auditor of auditos section   ==================================
# Auditor of auditos section
# Auditor of auditos section

# Auditor of auditos section
def AuditorsPractices(request):
    consolidatedgncobj = models.Auditorofauditors.objects.all()
    consolidatedgncobjnumber = models.Auditorofauditors.objects.all().count()
    #
    # CRITICAL_LEVELS = (
    #     ('low', 'low'),
    #     ('medium', 'medium'),
    #     ('high', 'high'),
    # )
    # QUARTERS = (
    #     ('Q1', 'Q1'),
    #     ('Q2', 'Q2'),
    #     ('Q3', 'Q3'),
    #     ('Q4', 'Q4'),
    # )
    # ROOT_CAUSE_ANALYSIS = (
    #     ('POCESSES', 'POCESSES'),
    #     ('PEOPLE', 'PEOPLE'),
    #     ('TECHNOLOGY', 'TECHNOLOGY'),
    # )

    # counting the number practices at different levels of current_status_at_xy
    mediumimpactissues = models.Auditorofauditors.objects.filter(
        current_status_at_xy='PENDING',
    ).count()
    highimpactissues = models.Auditorofauditors.objects.filter(
        current_status_at_xy='CLOSED',
    ).count()
    lowimpactissues = models.Auditorofauditors.objects.filter(
        current_status_at_xy='PARTIALLY_IMPLEMENTED',
    ).count()

    # counting the number practices at different levels of current_status_at_xy
    # RECOMMENDATION_STATE = (
    #     ('PARTIALLY_IMPLEMENTED', 'PARTIALLY_IMPLEMENTED'),
    #     ('PENDING', 'PENDING'),
    #     ('CLOSED', 'CLOSED'),
    # )
    PENDING = models.Auditorofauditors.objects.filter(
        current_status_at_xy='PENDING',
    ).count()
    CLOSED = models.Auditorofauditors.objects.filter(
        current_status_at_xy='CLOSED',
    ).count()
    PARTIALLY_IMPLEMENTED = models.Auditorofauditors.objects.filter(
        current_status_at_xy='PARTIALLY_IMPLEMENTED',
    ).count()
    # percentage of completed recos
    percentagecompleted = round((CLOSED / consolidatedgncobjnumber) * 100, 1)

    # ageing days total

    for totaldays in consolidatedgncobj:
        totaldays = +totaldays.ageing_days

    return render(request=request, template_name="governanceandcontrol/auditpractices.html",
                  context={
                      "consolidateddata": consolidatedgncobj,
                      "consolidatedgncobjnumber": consolidatedgncobjnumber,

                      # issues
                      "mediumimpactissues": mediumimpactissues,
                      "highimpactissues": highimpactissues,
                      "lowimpactissues": lowimpactissues,

                      # reommendations
                      "PARTIALLY_IMPLEMENTED": PARTIALLY_IMPLEMENTED,
                      "PENDING": PENDING,
                      "CLOSED": CLOSED,
                      "percentagecompleted": percentagecompleted,

                      # reommendations
                      "totaldays": round(totaldays, 1),

                  })


# Auditor of auditos section
def AuditorsRecommendations(request):
    consolidatedgncobj = models.GncTable.objects.all()
    consolidatedgncobjnumber = models.GncTable.objects.all().count()
    #
    # CRITICAL_LEVELS = (
    #     ('low', 'low'),
    #     ('medium', 'medium'),
    #     ('high', 'high'),
    # )
    # QUARTERS = (
    #     ('Q1', 'Q1'),
    #     ('Q2', 'Q2'),
    #     ('Q3', 'Q3'),
    #     ('Q4', 'Q4'),
    # )
    # ROOT_CAUSE_ANALYSIS = (
    #     ('POCESSES', 'POCESSES'),
    #     ('PEOPLE', 'PEOPLE'),
    #     ('TECHNOLOGY', 'TECHNOLOGY'),
    # )

    # counting the number issues at different levels of criticality
    mediumimpactissues = models.GncTable.objects.filter(
        criticality='medium',
    ).count()
    highimpactissues = models.GncTable.objects.filter(
        criticality='high',
    ).count()
    lowimpactissues = models.GncTable.objects.filter(
        criticality='low',
    ).count()

    # counting the number issues at different levels of state
    # RECOMMENDATION_STATE = (
    #     ('PARTIALLY_IMPLEMENTED', 'PARTIALLY_IMPLEMENTED'),
    #     ('PENDING', 'PENDING'),
    #     ('CLOSED', 'CLOSED'),
    # )
    PENDING = models.GncTable.objects.filter(
        recommendation_state='PENDING',
    ).count()
    CLOSED = models.GncTable.objects.filter(
        recommendation_state='CLOSED',
    ).count()
    PARTIALLY_IMPLEMENTED = models.GncTable.objects.filter(
        recommendation_state='PARTIALLY_IMPLEMENTED',
    ).count()
    # percentage of completed recos
    percentagecompleted = round((CLOSED / consolidatedgncobjnumber) * 100, 1)

    # ageing days total

    for totaldays in consolidatedgncobj:
        totaldays = +totaldays.ageing_days

    return render(request=request, template_name="governanceandcontrol/auditrecommendations.html",
                  context={
                      "consolidateddata": consolidatedgncobj,
                      "consolidatedgncobjnumber": consolidatedgncobjnumber,

                      # issues
                      "mediumimpactissues": mediumimpactissues,
                      "highimpactissues": highimpactissues,
                      "lowimpactissues": lowimpactissues,

                      # reommendations
                      "PARTIALLY_IMPLEMENTED": PARTIALLY_IMPLEMENTED,
                      "PENDING": PENDING,
                      "CLOSED": CLOSED,
                      "percentagecompleted": percentagecompleted,

                      # reommendations
                      "totaldays": round(totaldays, 1),

                  })


# Auditor of auditos section
def AuditorsConsolidated(request):
    consolidatedgncobj = models.GncTable.objects.all()
    consolidatedgncobjnumber = models.GncTable.objects.all().count()
    #
    # CRITICAL_LEVELS = (
    #     ('low', 'low'),
    #     ('medium', 'medium'),
    #     ('high', 'high'),
    # )
    # QUARTERS = (
    #     ('Q1', 'Q1'),
    #     ('Q2', 'Q2'),
    #     ('Q3', 'Q3'),
    #     ('Q4', 'Q4'),
    # )
    # ROOT_CAUSE_ANALYSIS = (
    #     ('POCESSES', 'POCESSES'),
    #     ('PEOPLE', 'PEOPLE'),
    #     ('TECHNOLOGY', 'TECHNOLOGY'),
    # )

    # counting the number issues at different levels of criticality
    mediumimpactissues = models.GncTable.objects.filter(
        criticality='medium',
    ).count()
    highimpactissues = models.GncTable.objects.filter(
        criticality='high',
    ).count()
    lowimpactissues = models.GncTable.objects.filter(
        criticality='low',
    ).count()

    # counting the number issues at different levels of state
    # RECOMMENDATION_STATE = (
    #     ('PARTIALLY_IMPLEMENTED', 'PARTIALLY_IMPLEMENTED'),
    #     ('PENDING', 'PENDING'),
    #     ('CLOSED', 'CLOSED'),
    # )
    PENDING = models.GncTable.objects.filter(
        recommendation_state='PENDING',
    ).count()
    CLOSED = models.GncTable.objects.filter(
        recommendation_state='CLOSED',
    ).count()
    PARTIALLY_IMPLEMENTED = models.GncTable.objects.filter(
        recommendation_state='PARTIALLY_IMPLEMENTED',
    ).count()
    # percentage of completed recos
    percentagecompleted = round((CLOSED / consolidatedgncobjnumber) * 100, 1)

    # ageing days total

    for totaldays in consolidatedgncobj:
        totaldays = +totaldays.ageing_days

    return render(request=request, template_name="governanceandcontrol/auditconsolidated.html",
                  context={
                      "consolidateddata": consolidatedgncobj,
                      "consolidatedgncobjnumber": consolidatedgncobjnumber,

                      # issues
                      "mediumimpactissues": mediumimpactissues,
                      "highimpactissues": highimpactissues,
                      "lowimpactissues": lowimpactissues,

                      # reommendations
                      "PARTIALLY_IMPLEMENTED": PARTIALLY_IMPLEMENTED,
                      "PENDING": PENDING,
                      "CLOSED": CLOSED,
                      "percentagecompleted": percentagecompleted,

                      # reommendations
                      "totaldays": round(totaldays, 1),

                  })


# ======================Details views===========================

def GoverncontrolprojectsDetail(request,id):
    consolidatedgncobj = models.GncTable.objects.get(id=id)
    # consolidatedgncobjnumber = models.GncTable.objects.all().count()
    #
    # CRITICAL_LEVELS = (
    #     ('low', 'low'),
    #     ('medium', 'medium'),
    #     ('high', 'high'),
    # )
    # QUARTERS = (
    #     ('Q1', 'Q1'),
    #     ('Q2', 'Q2'),
    #     ('Q3', 'Q3'),
    #     ('Q4', 'Q4'),
    # )
    # ROOT_CAUSE_ANALYSIS = (
    #     ('POCESSES', 'POCESSES'),
    #     ('PEOPLE', 'PEOPLE'),
    #     ('TECHNOLOGY', 'TECHNOLOGY'),
    # )

    # counting the number issues at different levels of criticality
    # mediumimpactissues = models.GncTable.objects.filter(
    #     criticality='medium',
    # ).count()
    # highimpactissues = models.GncTable.objects.filter(
    #     criticality='high',
    # ).count()
    # lowimpactissues = models.GncTable.objects.filter(
    #     criticality='low',
    # ).count()

    # counting the number issues at different levels of state
    # RECOMMENDATION_STATE = (
    #     ('PARTIALLY_IMPLEMENTED', 'PARTIALLY_IMPLEMENTED'),
    #     ('PENDING', 'PENDING'),
    #     ('CLOSED', 'CLOSED'),
    # )
    # PENDING = models.GncTable.objects.filter(
    #     recommendation_state='PENDING',
    # ).count()
    # CLOSED = models.GncTable.objects.filter(
    #     recommendation_state='CLOSED',
    # ).count()
    # PARTIALLY_IMPLEMENTED = models.GncTable.objects.filter(
    #     recommendation_state='PARTIALLY_IMPLEMENTED',
    # ).count()
    # percentage of completed recos
    # percentagecompleted = round((CLOSED / consolidatedgncobjnumber) * 100, 1)

    # ageing days total

    # for totaldays in consolidatedgncobj:
    #     totaldays = +totaldays.ageing_days

    return render(request=request, template_name="governanceandcontrol/governcontrolprojectsdetails.html",
                  context={
                      "consolidateddata": consolidatedgncobj,
                  #     "consolidatedgncobjnumber": consolidatedgncobjnumber,
                  #
                  #     # issues
                  #     "mediumimpactissues": mediumimpactissues,
                  #     "highimpactissues": highimpactissues,
                  #     "lowimpactissues": lowimpactissues,
                  #
                  #     # reommendations
                  #     "PARTIALLY_IMPLEMENTED": PARTIALLY_IMPLEMENTED,
                  #     "PENDING": PENDING,
                  #     "CLOSED": CLOSED,
                  #     "percentagecompleted": percentagecompleted,
                  #
                  #     # reommendations
                  #     "totaldays": round(totaldays, 1),
                  #
                  }
                  )


def GoverncontrolIssues(request):
    consolidatedgncobj = models.GncTable.objects.all()
    consolidatedgncobjnumber = models.GncTable.objects.all().count()
    #
    # CRITICAL_LEVELS = (
    #     ('low', 'low'),
    #     ('medium', 'medium'),
    #     ('high', 'high'),
    # )
    # QUARTERS = (
    #     ('Q1', 'Q1'),
    #     ('Q2', 'Q2'),
    #     ('Q3', 'Q3'),
    #     ('Q4', 'Q4'),
    # )
    # ROOT_CAUSE_ANALYSIS = (
    #     ('POCESSES', 'POCESSES'),
    #     ('PEOPLE', 'PEOPLE'),
    #     ('TECHNOLOGY', 'TECHNOLOGY'),
    # )

    # counting the number issues at different levels of criticality
    mediumimpactissues = models.GncTable.objects.filter(
        criticality='medium',
    ).count()
    highimpactissues = models.GncTable.objects.filter(
        criticality='high',
    ).count()
    lowimpactissues = models.GncTable.objects.filter(
        criticality='low',
    ).count()

    # counting the number issues at different levels of state
    # RECOMMENDATION_STATE = (
    #     ('PARTIALLY_IMPLEMENTED', 'PARTIALLY_IMPLEMENTED'),
    #     ('PENDING', 'PENDING'),
    #     ('CLOSED', 'CLOSED'),
    # )
    PENDING = models.GncTable.objects.filter(
        recommendation_state='PENDING',
    ).count()
    CLOSED = models.GncTable.objects.filter(
        recommendation_state='CLOSED',
    ).count()
    PARTIALLY_IMPLEMENTED = models.GncTable.objects.filter(
        recommendation_state='PARTIALLY_IMPLEMENTED',
    ).count()
    # percentage of completed recos
    percentagecompleted = round((CLOSED / consolidatedgncobjnumber) * 100, 1)

    # ageing days total

    for totaldays in consolidatedgncobj:
        totaldays = +totaldays.ageing_days

    return render(request=request, template_name="governanceandcontrol/governcontrolissues.html",
                  context={
                      "consolidateddata": consolidatedgncobj,
                      "consolidatedgncobjnumber": consolidatedgncobjnumber,

                      # issues
                      "mediumimpactissues": mediumimpactissues,
                      "highimpactissues": highimpactissues,
                      "lowimpactissues": lowimpactissues,

                      # reommendations
                      "PARTIALLY_IMPLEMENTED": PARTIALLY_IMPLEMENTED,
                      "PENDING": PENDING,
                      "CLOSED": CLOSED,
                      "percentagecompleted": percentagecompleted,

                      # reommendations
                      "totaldays": round(totaldays, 1),

                  })


def GoverncontrolrecommendationsDetails(request, id):
    consolidatedgncobj = models.GncTable.objects.get(id=id)
    # consolidatedgncobjnumber = models.GncTable.objects.all().count()
    #
    # CRITICAL_LEVELS = (
    #     ('low', 'low'),
    #     ('medium', 'medium'),
    #     ('high', 'high'),
    # )
    # QUARTERS = (
    #     ('Q1', 'Q1'),
    #     ('Q2', 'Q2'),
    #     ('Q3', 'Q3'),
    #     ('Q4', 'Q4'),
    # )
    # ROOT_CAUSE_ANALYSIS = (
    #     ('POCESSES', 'POCESSES'),
    #     ('PEOPLE', 'PEOPLE'),
    #     ('TECHNOLOGY', 'TECHNOLOGY'),
    # )

    # counting the number issues at different levels of criticality
    # mediumimpactissues = models.GncTable.objects.filter(
    #     criticality='medium',
    # ).count()
    # highimpactissues = models.GncTable.objects.filter(
    #     criticality='high',
    # ).count()
    # lowimpactissues = models.GncTable.objects.filter(
    #     criticality='low',
    # ).count()

    # counting the number issues at different levels of state
    # RECOMMENDATION_STATE = (
    #     ('PARTIALLY_IMPLEMENTED', 'PARTIALLY_IMPLEMENTED'),
    #     ('PENDING', 'PENDING'),
    #     ('CLOSED', 'CLOSED'),
    # )
    # PENDING = models.GncTable.objects.filter(
    #     recommendation_state='PENDING',
    # ).count()
    # CLOSED = models.GncTable.objects.filter(
    #     recommendation_state='CLOSED',
    # ).count()
    # PARTIALLY_IMPLEMENTED = models.GncTable.objects.filter(
    #     recommendation_state='PARTIALLY_IMPLEMENTED',
    # ).count()
    # # percentage of completed recos
    # percentagecompleted = round((CLOSED / consolidatedgncobjnumber) * 100, 1)

    # ageing days total

    # for totaldays in consolidatedgncobj:
    #     totaldays = +totaldays.ageing_days

    return render(request=request, template_name="governanceandcontrol/governcontrolprojectsdetails.html",
                  context={
                      "consolidateddata": consolidatedgncobj,
                      #   "consolidatedgncobjnumber": consolidatedgncobjnumber,

                      #   # issues
                      #   "mediumimpactissues": mediumimpactissues,
                      #   "highimpactissues": highimpactissues,
                      #   "lowimpactissues": lowimpactissues,

                      #   # reommendations
                      #   "PARTIALLY_IMPLEMENTED": PARTIALLY_IMPLEMENTED,
                      #   "PENDING": PENDING,
                      #   "CLOSED": CLOSED,
                      #   "percentagecompleted": percentagecompleted,

                      #   # reommendations
                      #   "totaldays": round(totaldays,1),

                  })
