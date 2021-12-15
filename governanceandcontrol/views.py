import days as days
from django.shortcuts import render
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import  GncTableForm
from django.contrib.auth import login, authenticate, logout  # add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def dashboard(request):
    gncobj = models.GncTable.objects.all()
    # info =
    return render(request, 'governanceandcontrol/index.html', {
        "gncojbects": gncobj
    })



@login_required
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

@login_required
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

@login_required
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

    return render(request=request, template_name="governanceandcontrol/governcontrolrecommendations.html",
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

@login_required
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


# ======================Details views===========================
@login_required
def GoverncontrolprojectsDetail(request, id):
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

@login_required
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

@login_required
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

@login_required
def AddGoverncontrolprojects(request):
    if request.method == "POST":
        form = GncTableForm(request.POST)
        if form.is_valid():
            governcontrolproject = form.save(commit=True)
            return redirect('governcontrolprojectsdetails', governcontrolproject.pk)
    else:
        form = GncTableForm()
    return render(request, 'governanceandcontrol/addformgovernanceandcontrol.html',{'form': form})


