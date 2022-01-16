from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from . import models

from .forms import AuditorofauditorsForm
from .models import Auditorofauditors

# Create your views here.

# ====================================== Auditor of auditos section   ==================================
# Auditor of auditos section
# Auditor of auditos section

# Auditor of auditos section
@login_required
def AuditorsPractices(request):
    consolidatedgncobj = models.Auditorofauditors.objects.all()
    consolidatedgncobjnumber = models.Auditorofauditors.objects.all().count()

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
        try:
            percentagecompleted = round((CLOSED / consolidatedgncobjnumber) * 100, 1)
        except ZeroDivisionError:
            percentagecompleted = 0

        # ageing days total

        for totaldays in consolidatedgncobj:
            totaldays = +totaldays.ageing_days

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
    consolidatedgncobj = models.Auditorofauditors.objects.all()
    consolidatedgncobjnumber = models.Auditorofauditors.objects.all().count()

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
        mediumimpactissues = models.Auditorofauditors.objects.filter(
            current_status_at_xy='PARTIALLY_IMPLEMENTED',
        ).count()
        highimpactissues = models.Auditorofauditors.objects.filter(
            current_status_at_xy='PENDING',
        ).count()
        lowimpactissues = models.Auditorofauditors.objects.filter(
            current_status_at_xy='CLOSED',
        ).count()

        # counting the number issues at different levels of state
        # RECOMMENDATION_STATE = (
        #     ('PARTIALLY_IMPLEMENTED', 'PARTIALLY_IMPLEMENTED'),
        #     ('PENDING', 'PENDING'),
        #     ('CLOSED', 'CLOSED'),
        # )
        PENDING = models.Auditorofauditors.objects.filter(
            recommendation_state='PENDING',
        ).count()
        CLOSED = models.Auditorofauditors.objects.filter(
            recommendation_state='CLOSED',
        ).count()
        PARTIALLY_IMPLEMENTED = models.Auditorofauditors.objects.filter(
            recommendation_state='PARTIALLY_IMPLEMENTED',
        ).count()
        # percentage of completed recos
        try:
            percentagecompleted = round((CLOSED / consolidatedgncobjnumber) * 100, 1)
        except ZeroDivisionError:
            percentagecompleted = 0

        # ageing days total

        for totaldays in consolidatedgncobj:
            totaldays =+totaldays.ageing_days

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
    consolidatedgncobj = models.Auditorofauditors.objects.all()
    consolidatedgncobjnumber = models.Auditorofauditors.objects.all().count()

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
        mediumimpactissues = models.Auditorofauditors.objects.filter(
            criticality='medium',
        ).count()
        highimpactissues = models.Auditorofauditors.objects.filter(
            criticality='high',
        ).count()
        lowimpactissues = models.Auditorofauditors.objects.filter(
            criticality='low',
        ).count()

        # counting the number issues at different levels of state
        # RECOMMENDATION_STATE = (
        #     ('PARTIALLY_IMPLEMENTED', 'PARTIALLY_IMPLEMENTED'),
        #     ('PENDING', 'PENDING'),
        #     ('CLOSED', 'CLOSED'),
        # )
        PENDING = models.Auditorofauditors.objects.filter(
            recommendation_state='PENDING',
        ).count()
        CLOSED = models.Auditorofauditors.objects.filter(
            recommendation_state='CLOSED',
        ).count()
        PARTIALLY_IMPLEMENTED = models.Auditorofauditors.objects.filter(
            recommendation_state='PARTIALLY_IMPLEMENTED',
        ).count()
        # percentage of completed recos
        try:
            percentagecompleted = round((CLOSED / consolidatedgncobjnumber) * 100, 1)
        except ZeroDivisionError:
            percentagecompleted = 0
        # ageing days total

        for totaldays in consolidatedgncobj:
            totaldays =+totaldays.ageing_days

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
    consolidatedgncobj = models.Auditorofauditors.objects.get(id=id)

    return render(request=request, template_name="auditorofauditor/auditOfauditosdetails.html",
                  context={ "consolidateddata": consolidatedgncobj,}
                  )


@login_required
def AddAuditor_of_auditorsDetail(request):
    if request.method == "POST":
        form = AuditorofauditorsForm(request.POST)
        if form.is_valid():
            auditorofauditors = form.save(commit=True)
            return redirect('auditOfauditosdetails', auditorofauditors.pk)
    else:
        form = AuditorofauditorsForm()
    return render(request, 'auditorofauditor/addformauditor.html', {'form': form})


