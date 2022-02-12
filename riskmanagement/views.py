from django.shortcuts import render
from . import models
# import days as days
from django.shortcuts import render
from . import models
from . import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout  # add this
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import RiskManagementForm

# Create your views here.

# IMPACT_LEVELS = (
#     ('low', 'low'),
#     ('moderate', 'moderate'),
#     ('high', 'high'),
# )
# RATE_LEVELS = (
#     ('low', 'low'),
#     ('moderate', 'moderate'),
#     ('high', 'high'),
# )
# LIKELIHOOD = (
#     ('low', 'low'),
#     ('moderate', 'moderate'),
#     ('high', 'high'),
# )
# CONTROL_EXISTANCE = (
#     ('yes', 'yes'),
#     ('no', 'no'),
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
# RECOMMENDATION_STATE = (
#     ('PARTIALLY_IMPLEMENTED', 'PARTIALLY_IMPLEMENTED'),
#     ('PENDING', 'PENDING'),
#     ('CLOSED', 'CLOSED'),
# )


# Risk management section
@login_required
def Risks(request):
    consolidatedgncobj = models.RiskManagement.objects.all()
    consolidatedgncobjnumber = models.RiskManagement.objects.all().count()
    if not consolidatedgncobj:
        return render(request=request, template_name="riskmanagement/risks.html",
                      context={
                          "consolidateddata": {},
                          "consolidatedgncobjnumber": 0,

                          # issues
                          "mediumimpactissues": 0,
                          "highimpactissues": 0,
                          "lowimpactissues": 0,

                          # reommendations
                          "PARTIALLY_IMPLEMENTED": 0,
                          "PENDING": 0,
                          "CLOSED": 0,
                          "percentagecompleted": 0,

                          # reommendations
                          "totaldays": 0,

                      }
                      )
    else:
        # counting the number issues at different levels of criticality
        mediumimpactissues = models.RiskManagement.objects.filter(
            impact='medium',
        ).count()
        highimpactissues = models.RiskManagement.objects.filter(
            impact='high',
        ).count()
        lowimpactissues = models.RiskManagement.objects.filter(
            impact='low',
        ).count()

        # LIKELIHOOD = (
        #     ('low', 'low'),
        #     ('moderate', 'moderate'),
        #     ('high', 'high'),
        # )
        PENDING = models.RiskManagement.objects.filter(
            likelihood='low',
        ).count()
        CLOSED = models.RiskManagement.objects.filter(
            likelihood='high',
        ).count()
        PARTIALLY_IMPLEMENTED = models.RiskManagement.objects.filter(
            likelihood='moderate',
        ).count()
        # percentage of completed recos
        percentagecompleted = round((CLOSED / consolidatedgncobjnumber) * 100, 1)

        # ageing days total

        # for totaldays in consolidatedgncobj:
        #     totaldays = +totaldays.ageing_days

        return render(request=request, template_name="riskmanagement/risks.html",
                      context={
                          "consolidateddata": consolidatedgncobj,
                          "consolidatedgncobjnumber": consolidatedgncobjnumber,

                          # impact_levels
                          "mediumimpactissues": mediumimpactissues,
                          "highimpactissues": highimpactissues,
                          "lowimpactissues": lowimpactissues,

                          # reommendations
                          "PARTIALLY_IMPLEMENTED": PARTIALLY_IMPLEMENTED,
                          "PENDING": PENDING,
                          "CLOSED": CLOSED,
                          "percentagecompleted": percentagecompleted,

                          # reommendations
                          # "totaldays": round(totaldays, 1),

                      })


# Risk management section
@login_required
def RiskControl(request):
    consolidatedgncobj = models.RiskManagement.objects.all()
    consolidatedgncobjnumber = models.RiskManagement.objects.all().count()
    if not consolidatedgncobj:
        return render(request=request, template_name="riskmanagement/riskcontrol.html",
                      context={
                          "consolidateddata": {},
                          "consolidatedgncobjnumber": 0,

                          # issues
                          "mediumimpactissues": 0,
                          "highimpactissues": 0,
                          "lowimpactissues": 0,

                          # reommendations
                          "PARTIALLY_IMPLEMENTED": 0,
                          "PENDING": 0,
                          "CLOSED": 0,
                          "percentagecompleted": 0,

                          # reommendations
                          "totaldays": 0,

                      }
                      )
    else:

        # counting the number issues at different levels of criticality
        mediumimpactissues = models.RiskManagement.objects.filter(
            impact='medium',
        ).count()
        highimpactissues = models.RiskManagement.objects.filter(
            impact='high',
        ).count()
        lowimpactissues = models.RiskManagement.objects.filter(
            impact='low',
        ).count()

        # counting the number issues at different levels of state
        # RECOMMENDATION_STATE = (
        #     ('PARTIALLY_IMPLEMENTED', 'PARTIALLY_IMPLEMENTED'),
        #     ('PENDING', 'PENDING'),
        #     ('CLOSED', 'CLOSED'),
        # )

        # ageing days total

        # for totaldays in consolidatedgncobj:
        #     totaldays = +totaldays.ageing_days

        return render(request=request, template_name="riskmanagement/riskcontrol.html",
                      context={
                          "consolidateddata": consolidatedgncobj,
                          "consolidatedgncobjnumber": consolidatedgncobjnumber,

                          # issues
                          "mediumimpactissues": mediumimpactissues,
                          "highimpactissues": highimpactissues,
                          "lowimpactissues": lowimpactissues,

                          # reommendations


                          # reommendations
                          # "totaldays": round(totaldays, 1),

                      })


# Risk management section
@login_required
def KRI(request):
    consolidatedgncobj = models.RiskManagement.objects.all()
    consolidatedgncobjnumber = models.RiskManagement.objects.all().count()
    #
    if not consolidatedgncobj:
        return render(request=request, template_name="riskmanagement/riskkri.html",
                      context={
                          "consolidateddata": {},
                          "consolidatedgncobjnumber": 0,

                          # issues
                          "mediumimpactissues": 0,
                          "highimpactissues": 0,
                          "lowimpactissues": 0,

                          # reommendations
                          "PARTIALLY_IMPLEMENTED": 0,
                          "PENDING": 0,
                          "CLOSED": 0,
                          "percentagecompleted": 0,

                          # reommendations
                          "totaldays": 0,

                      }
                      )
    else:

        # counting the number issues at different levels of criticality
        mediumimpactissues = models.RiskManagement.objects.filter(
            impact='medium',
        ).count()
        highimpactissues = models.RiskManagement.objects.filter(
            impact='high',
        ).count()
        lowimpactissues = models.RiskManagement.objects.filter(
            impact='low',
        ).count()


        # ageing days total

        # for totaldays in consolidatedgncobj:
        #     totaldays = +totaldays.ageing_days

        return render(request=request, template_name="riskmanagement/riskkri.html",
                      context={
                          "consolidateddata": consolidatedgncobj,
                          "consolidatedgncobjnumber": consolidatedgncobjnumber,

                          # issues
                          "mediumimpactissues": mediumimpactissues,
                          "highimpactissues": highimpactissues,
                          "lowimpactissues": lowimpactissues,


                      })



# ======================Details views===========================
@login_required
def RisksDetail(request, id):
    consolidatedgncobj = models.RiskManagement.objects.get(id=id)

    return render(request=request, template_name="riskmanagement/risksdetails.html",
                  context={ "consolidateddata": consolidatedgncobj,}
                  )


@login_required
def AddRiskRecords(request):
    if request.method == "POST":
        form = RiskManagementForm(request.POST)
        if form.is_valid():
            riskmanagementrecord = form.save(commit=True)
            return redirect('riskmanagement:risksdetails', riskmanagementrecord.pk)
    else:
        form = RiskManagementForm()
    return render(request, 'riskmanagement/addformrisk.html', {'form': form})


