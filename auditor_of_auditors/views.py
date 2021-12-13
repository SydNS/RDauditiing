from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from . import models

# Create your views here.

# ====================================== Auditor of auditos section   ==================================
# Auditor of auditos section
# Auditor of auditos section

# Auditor of auditos section
@login_required
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
@login_required
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
@login_required
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

