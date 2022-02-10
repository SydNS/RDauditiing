# import days as days
from django.shortcuts import render
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import Governance_And_ControlForm
from django.contrib.auth import login, authenticate, logout  # add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from riskmanagement.models import RiskManagement
from auditor_of_auditors.models import Auditor_of_auditors
from accounts.models import Department
from accounts.models import Person
from accounts.models import RatingUser
# importing datetime module
import datetime


# Create your views here.
@login_required
def dashboard(request):
    consolidatedgncobj = models.Governance_And_Control.objects.all()
    if not consolidatedgncobj:
        return render(request=request, template_name="governanceandcontrol/index.html",
                      context={

                          # ============# governanceandcontrol========================================
                          "gncojbects": {},
                          "gncobjnumber": 0,
                          # issues
                          "mediumimpactissues": 5,
                          "highimpactissues": 10,
                          "lowimpactissues": 20,

                          # highimpactprojects
                          "highimpactprojects": {},

                          # likelihood
                          "risklikelihoodmoderate": 40,
                          "risklikelihoodlow": 20,
                          "risklikelihoodhigh": 60,

                          # reommendations
                          "PARTIALLY_IMPLEMENTED": 15,
                          "PENDING": 20,
                          "CLOSED": 10,
                          "percentagecompleted": 0,

                          # reommendations
                          "totaldays": round(0, 1),

                          # ========================# riskmanagement================================

                          "riskobj": {},
                          "riskobjnumber": 0,
                          # issues
                          "riskmediumimpactissues": 0,
                          "riskhighimpactissues": 0,
                          "risklowimpactissues": 0,

                          "AoAobj": {},
                          "Deptobj": {},
                          "Personobj": {},
                          "Gradingobj": {},
                      }
                      )
    else:
        gncobj = models.Governance_And_Control.objects.all()
        gncobjnumber = models.Governance_And_Control.objects.all().count()

        highimpactprojects = models.Governance_And_Control.objects.filter(
            criticality='high',
        )

        mediumimpactissues = models.Governance_And_Control.objects.filter(
            criticality='medium',
        ).count()
        highimpactissues = models.Governance_And_Control.objects.filter(
            criticality='high',
        ).count()
        lowimpactissues = models.Governance_And_Control.objects.filter(
            criticality='low',
        ).count()
        PENDING = models.Governance_And_Control.objects.filter(
            recommendation_state='PENDING',
        ).count()
        CLOSED = models.Governance_And_Control.objects.filter(
            recommendation_state='CLOSED',
        ).count()
        PARTIALLY_IMPLEMENTED = models.Governance_And_Control.objects.filter(
            recommendation_state='PARTIALLY_IMPLEMENTED',
        ).count()
        # percentage of completed recos
        try:
            percentagecompleted = round((CLOSED / gncobjnumber) * 100, 1)
        except ZeroDivisionError:
            percentagecompleted = 0

        # ageing days total

        for totaldays in gncobj:
            totaldays = +totaldays.ageing_days

        # ===========================================# riskmanagement===============================================================================

        riskobj = RiskManagement.objects.all()
        riskobjnumber = RiskManagement.objects.all().count()

        # counting the number issues at different levels of criticality
        riskmediumimpactissues = RiskManagement.objects.filter(
            impact='medium',
        ).count()
        riskhighimpactissues = RiskManagement.objects.filter(
            impact='high',
        ).count()
        risklowimpactissues = RiskManagement.objects.filter(
            impact='low',
        ).count()
        # likelihood
        xy_strategic_pillar = RiskManagement.objects.filter(
            xy_strategic_pillar='low',
        ).count()
        risklikelihoodhigh = RiskManagement.objects.filter(
            likelihood='high',
        ).count()
        risklikelihoodmoderate = RiskManagement.objects.filter(
            likelihood='moderate',
        ).count()
        risklikelihoodlow = RiskManagement.objects.filter(
            likelihood='low',
        ).count()

        AoAobj = Auditor_of_auditors.objects.all()

        Deptobj = Dept.objects.all()
        Personobj = Person.objects.all()
        Gradingobj = GradingUser.objects.all()

        # info =
        return render(request, 'governanceandcontrol/index.html', {

            # ============# governanceandcontrol========================================
            "gncojbects": gncobj,
            "gncobjnumber": gncobjnumber,
            # issues
            "mediumimpactissues": mediumimpactissues,
            "highimpactissues": highimpactissues,
            "lowimpactissues": lowimpactissues,

            # highimpactprojects
            "highimpactprojects": highimpactprojects,

            # likelihood
            "risklikelihoodmoderate": risklikelihoodmoderate,
            "risklikelihoodlow": risklikelihoodlow,
            "risklikelihoodhigh": risklikelihoodhigh,

            # reommendations
            "PARTIALLY_IMPLEMENTED": PARTIALLY_IMPLEMENTED,
            "PENDING": PENDING,
            "CLOSED": CLOSED,
            "percentagecompleted": percentagecompleted,

            # reommendations
            "totaldays": round(totaldays, 1),

            # ========================# riskmanagement================================

            "riskobj": riskobj,
            "riskobjnumber": riskobjnumber,
            # issues
            "riskmediumimpactissues": riskmediumimpactissues,
            "riskhighimpactissues": riskhighimpactissues,
            "risklowimpactissues": risklowimpactissues,

            "AoAobj": AoAobj,
            "Deptobj": Deptobj,
            "Personobj": Personobj,
            "Gradingobj": Gradingobj,
        })


# ==================================================GNC========================================================
@login_required
def Governcontrolprojects(request):
    consolidatedgncobj = models.Governance_And_Control.objects.all()
    consolidatedgncobjnumber = models.Governance_And_Control.objects.all().count()
    if not consolidatedgncobj:
        return render(request=request, template_name="governanceandcontrol/governcontrolprojects.html",
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
        mediumimpactissues = models.Governance_And_Control.objects.filter(
            criticality='medium',
        ).count()
        highimpactissues = models.Governance_And_Control.objects.filter(
            criticality='high',
        ).count()
        lowimpactissues = models.Governance_And_Control.objects.filter(
            criticality='low',
        ).count()

        # counting the number issues at different levels of state
        # RECOMMENDATION_STATE = (
        #     ('PARTIALLY_IMPLEMENTED', 'PARTIALLY_IMPLEMENTED'),
        #     ('PENDING', 'PENDING'),
        #     ('CLOSED', 'CLOSED'),
        # )
        PENDING = models.Governance_And_Control.objects.filter(
            recommendation_state='PENDING',
        ).count()
        CLOSED = models.Governance_And_Control.objects.filter(
            recommendation_state='CLOSED',
        ).count()
        PARTIALLY_IMPLEMENTED = models.Governance_And_Control.objects.filter(
            recommendation_state='PARTIALLY_IMPLEMENTED',
        ).count()
        # percentage of completed recos
        try:
            percentagecompleted = round((CLOSED / consolidatedgncobjnumber) * 100, 1)
        except ZeroDivisionError:
            percentagecompleted = 0

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
    consolidatedgncobj = models.Governance_And_Control.objects.all()
    consolidatedgncobjnumber = models.Governance_And_Control.objects.all().count()

    if not consolidatedgncobj:
        return render(request=request, template_name="governanceandcontrol/governcontrolprojects.html",
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
        mediumimpactissues = models.Governance_And_Control.objects.filter(
            criticality='medium',
        ).count()
        highimpactissues = models.Governance_And_Control.objects.filter(
            criticality='high',
        ).count()
        lowimpactissues = models.Governance_And_Control.objects.filter(
            criticality='low',
        ).count()

        PENDING = models.Governance_And_Control.objects.filter(
            recommendation_state='PENDING',
        ).count()
        CLOSED = models.Governance_And_Control.objects.filter(
            recommendation_state='CLOSED',
        ).count()
        PARTIALLY_IMPLEMENTED = models.Governance_And_Control.objects.filter(
            recommendation_state='PARTIALLY_IMPLEMENTED',
        ).count()
        # percentage of completed recos
        # percentage of completed recos
        try:
            percentagecompleted = round((CLOSED / consolidatedgncobjnumber) * 100, 1)
        except ZeroDivisionError:
            percentagecompleted = 0

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
    consolidatedgncobj = models.Governance_And_Control.objects.all()
    consolidatedgncobjnumber = models.Governance_And_Control.objects.all().count()

    if not consolidatedgncobj:
        return render(request=request, template_name="governanceandcontrol/governcontrolprojects.html",
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
        mediumimpactissues = models.Governance_And_Control.objects.filter(
            criticality='medium',
        ).count()
        highimpactissues = models.Governance_And_Control.objects.filter(
            criticality='high',
        ).count()
        lowimpactissues = models.Governance_And_Control.objects.filter(
            criticality='low',
        ).count()
        PENDING = models.Governance_And_Control.objects.filter(
            recommendation_state='PENDING',
        ).count()
        CLOSED = models.Governance_And_Control.objects.filter(
            recommendation_state='CLOSED',
        ).count()
        PARTIALLY_IMPLEMENTED = models.Governance_And_Control.objects.filter(
            recommendation_state='PARTIALLY_IMPLEMENTED',
        ).count()
        # percentage of completed recos
        try:
            percentagecompleted = round((CLOSED / consolidatedgncobjnumber) * 100, 1)
        except ZeroDivisionError:
            percentagecompleted = 0

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
    consolidatedgncobj = models.Governance_And_Control.objects.all()
    consolidatedgncobjnumber = models.Governance_And_Control.objects.all().count()
    if not consolidatedgncobj:
        return render(request=request, template_name="governanceandcontrol/governcontrolconsolidated.html",
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
        mediumimpactissues = models.Governance_And_Control.objects.filter(
            criticality='medium',
        ).count()
        highimpactissues = models.Governance_And_Control.objects.filter(
            criticality='high',
        ).count()
        lowimpactissues = models.Governance_And_Control.objects.filter(
            criticality='low',
        ).count()

        # counting the number issues at different levels of state
        # RECOMMENDATION_STATE = (
        #     ('PARTIALLY_IMPLEMENTED', 'PARTIALLY_IMPLEMENTED'),
        #     ('PENDING', 'PENDING'),
        #     ('CLOSED', 'CLOSED'),
        # )
        PENDING = models.Governance_And_Control.objects.filter(
            recommendation_state='PENDING',
        ).count()
        CLOSED = models.Governance_And_Control.objects.filter(
            recommendation_state='CLOSED',
        ).count()
        PARTIALLY_IMPLEMENTED = models.Governance_And_Control.objects.filter(
            recommendation_state='PARTIALLY_IMPLEMENTED',
        ).count()
        # percentage of completed recos
        # percentage of completed recos
        try:
            percentagecompleted = round((CLOSED / consolidatedgncobjnumber) * 100, 1)
        except ZeroDivisionError:
            percentagecompleted = 0

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
    consolidatedgncobj = models.Governance_And_Control.objects.get(id=id)

    return render(request=request, template_name="governanceandcontrol/governcontrolprojectsdetails.html",
                  context={"consolidateddata": consolidatedgncobj, }
                  )


@login_required
def GoverncontrolrecommendationsDetails(request, id):
    consolidatedgncobj = models.Governance_And_Control.objects.get(id=id)

    return render(request=request, template_name="governanceandcontrol/governcontrolprojectsdetails.html",
                  context={"consolidateddata": consolidatedgncobj, })


@login_required
def AddGoverncontrolprojects(request):
    if request.method == "POST":
        form = Governance_And_ControlForm(request.POST)
        if form.is_valid():
            governcontrolproject = form.save(commit=True)
            return redirect('governcontrolprojectsdetails', governcontrolproject.pk)
    else:
        form = Governance_And_ControlForm()
    return render(request, 'governanceandcontrol/addformgovernanceandcontrol.html', {'form': form})


@login_required
def FAQ(request):
    return render(request, 'governanceandcontrol/faq.html')
