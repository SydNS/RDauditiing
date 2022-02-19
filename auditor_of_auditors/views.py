from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from . import models

from .forms import Auditor_of_auditorsForm
from .models import Auditor_of_auditors


# Create your views here.

# ====================================== Auditor of auditos section   ==================================
# Auditor of auditos section
# Auditor of auditos section

# Auditor of auditos section
@login_required
def AuditorsPractices(request):
    consolidatedgncobj = models.Auditor_of_auditors.objects.all()
    consolidatedgncobjnumber = models.Auditor_of_auditors.objects.all().count()

    if not consolidatedgncobj:
        return render(request=request, template_name="auditorofauditor/auditpractices.html",
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
        # counting the number practices at different levels of current_status_at_xy
        mediumimpactissues = models.Auditor_of_auditors.objects.filter(
            current_status_at_xy='PENDING',
        ).count()
        highimpactissues = models.Auditor_of_auditors.objects.filter(
            current_status_at_xy='CLOSED',
        ).count()
        lowimpactissues = models.Auditor_of_auditors.objects.filter(
            current_status_at_xy='PARTIALLY_IMPLEMENTED',
        ).count()

        # counting the number practices at different levels of current_status_at_xy
        # RECOMMENDATION_STATE = (
        #     ('PARTIALLY_IMPLEMENTED', 'PARTIALLY_IMPLEMENTED'),
        #     ('PENDING', 'PENDING'),
        #     ('CLOSED', 'CLOSED'),
        # )
        PENDING = models.Auditor_of_auditors.objects.filter(
            current_status_at_xy='PENDING',
        ).count()
        CLOSED = models.Auditor_of_auditors.objects.filter(
            current_status_at_xy='CLOSED',
        ).count()
        PARTIALLY_IMPLEMENTED = models.Auditor_of_auditors.objects.filter(
            current_status_at_xy='PARTIALLY_IMPLEMENTED',
        ).count()
        # percentage of completed recos
        try:
            percentagecompleted = round((CLOSED / consolidatedgncobjnumber) * 100, 1)
        except ZeroDivisionError:
            percentagecompleted = 0

        # ageing days total
        totaldays = 0
        for x in consolidatedgncobj:
            totaldays += x.ageing_days
        print(totaldays)

        return render(request=request, template_name="auditorofauditor/auditpractices.html",
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
@login_required
def AuditorsRecommendations(request):
    consolidatedgncobj = models.Auditor_of_auditors.objects.all()
    consolidatedgncobjnumber = models.Auditor_of_auditors.objects.all().count()

    if not consolidatedgncobj:
        return render(request=request, template_name="auditorofauditor/auditrecommendations.html",
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

        # CURRENT_STATUS_XY = (
        #     ('PARTIALLY_IMPLEMENTED', 'PARTIALLY_IMPLEMENTED'),
        #     ('PENDING', 'PENDING'),
        #     ('CLOSED', 'CLOSED'),
        # )
        mediumimpactissues = models.Auditor_of_auditors.objects.filter(
            current_status_at_xy='PARTIALLY_IMPLEMENTED',
        ).count()
        highimpactissues = models.Auditor_of_auditors.objects.filter(
            current_status_at_xy='PENDING',
        ).count()
        lowimpactissues = models.Auditor_of_auditors.objects.filter(
            current_status_at_xy='CLOSED',
        ).count()

        # counting the number issues at different levels of state
        # RECOMMENDATION_STATE = (
        #     ('PARTIALLY_IMPLEMENTED', 'PARTIALLY_IMPLEMENTED'),
        #     ('PENDING', 'PENDING'),
        #     ('CLOSED', 'CLOSED'),
        # )
        PENDING = models.Auditor_of_auditors.objects.filter(
            recommendation_state='PENDING',
        ).count()
        CLOSED = models.Auditor_of_auditors.objects.filter(
            recommendation_state='CLOSED',
        ).count()
        PARTIALLY_IMPLEMENTED = models.Auditor_of_auditors.objects.filter(
            recommendation_state='PARTIALLY_IMPLEMENTED',
        ).count()
        # percentage of completed recos
        try:
            percentagecompleted = round((CLOSED / consolidatedgncobjnumber) * 100, 1)
        except ZeroDivisionError:
            percentagecompleted = 0

        # ageing days total

        totaldays = 0
        for x in consolidatedgncobj:
            totaldays += x.ageing_days
        print(totaldays)

        return render(request=request, template_name="auditorofauditor/auditrecommendations.html",
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
@login_required
def AuditorsConsolidated(request):
    consolidatedgncobj = models.Auditor_of_auditors.objects.all()
    consolidatedgncobjnumber = models.Auditor_of_auditors.objects.all().count()

    if not consolidatedgncobj:
        return render(request=request, template_name="auditorofauditor/auditconsolidated.html",
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
        mediumimpactissues = models.Auditor_of_auditors.objects.filter(
            current_status_at_xy='PARTIALLY_IMPLEMENTED',
        ).count()
        highimpactissues = models.Auditor_of_auditors.objects.filter(
            current_status_at_xy='PENDING',
        ).count()
        lowimpactissues = models.Auditor_of_auditors.objects.filter(
            current_status_at_xy='CLOSED',
        ).count()

        # counting the number issues at different levels of state
        # RECOMMENDATION_STATE = (
        #     ('PARTIALLY_IMPLEMENTED', 'PARTIALLY_IMPLEMENTED'),
        #     ('PENDING', 'PENDING'),
        #     ('CLOSED', 'CLOSED'),
        # )
        PENDING = models.Auditor_of_auditors.objects.filter(
            recommendation_state='PENDING',
        ).count()
        CLOSED = models.Auditor_of_auditors.objects.filter(
            recommendation_state='CLOSED',
        ).count()
        PARTIALLY_IMPLEMENTED = models.Auditor_of_auditors.objects.filter(
            recommendation_state='PARTIALLY_IMPLEMENTED',
        ).count()
        # percentage of completed recos
        try:
            percentagecompleted = round((CLOSED / consolidatedgncobjnumber) * 100, 1)
        except ZeroDivisionError:
            percentagecompleted = 0
        # ageing days total

        totaldays = 0
        for x in consolidatedgncobj:
            totaldays += x.ageing_days
        print(totaldays)

        return render(request=request, template_name="auditorofauditor/auditconsolidated.html",
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
def Auditor_of_auditorsDetail(request, id):
    consolidatedgncobj = models.Auditor_of_auditors.objects.get(id=id)

    return render(request=request, template_name="auditorofauditor/auditorofauditorsdetails.html",
                  context={"consolidateddata": consolidatedgncobj, }
                  )


@login_required
def AddAuditor_of_auditorsDetail(request):
    if request.method == "POST":
        form = Auditor_of_auditorsForm(request.POST)
        if form.is_valid():
            Auditor_of_auditors = form.save(commit=True)
            return redirect('auditor_of_auditors:auditOfauditosdetails', Auditor_of_auditors.pk)
    else:
        form = Auditor_of_auditorsForm()
    return render(request, 'auditorofauditor/addformauditor.html', {'form': form})


@login_required
def EditAuditor_of_auditorsDetail(request, id):
    consolidatedgncobj = models.Auditor_of_auditors.objects.get(id=id)
    if request.method == "POST":
        form = Auditor_of_auditorsForm(request.POST, instance=consolidatedgncobj)
        if form.is_valid():
            Auditor_of_auditors = form.save(commit=True)
            return redirect('auditor_of_auditors:auditorsofauditorsdetails', Auditor_of_auditors.pk)
    else:
        form = Auditor_of_auditorsForm(instance=consolidatedgncobj)
    return render(request, 'auditorofauditor/editformauditor.html', {'form': form})
