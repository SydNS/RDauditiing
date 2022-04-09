from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from . import models

# Register your models here.
from .models import Auditor_of_auditors, AuditngStandards

admin.site.site_header = 'Ruth Doreen Auditing Tool'


@admin.register(Auditor_of_auditors)
class AuditorofauditorsAdmin(ImportExportModelAdmin):
    list_display = ('internal_audit_leading_practices', 'iia_standards', 'current_status_at_xy', 'assessment',
                    'recommendations', 'action_plan', 'recommendation_state', 'agreed_implementation_date',
                    'revised_implementation_date', 'last_status_update', 'ageing_days'
                    , 'actual_implementation_date','owner', 'final_approver',
                    )
    list_filter = ('internal_audit_leading_practices','iia_standards', 'current_status_at_xy', 'ageing_days', )
    search_fields = ('internal_audit_leading_practices', 'iia_standards', 'current_status_at_xy', 'assessment',
                    'recommendations', 'action_plan', 'recommendation_state', 'agreed_implementation_date',
                    'revised_implementation_date', 'last_status_update', 'ageing_days'
                    , 'actual_implementation_date','owner', 'final_approver',
                    )

# @admin.register(AuditngStandards)
# class AAuditngStandardsAdmin(ImportExportModelAdmin):
#     list_display = ( 'link_to_standards',)


# class Auditorofauditors(models.Model):
#     internal_audit_leading_practices = models.CharField(db_column='Internal_audit_leading_Practices', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     iia_standards = models.CharField(db_column='IIA_Standards', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     current_status_at_xy = models.CharField(db_column='Current_Status_at_XY', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     assessment = models.CharField(db_column='Assessment', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     recommendations = models.CharField(db_column='Recommendations', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     action_plan = models.CharField(db_column='Action_Plan', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     recommendation_state = models.CharField(db_column='Recommendation_State', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     agreed_implementation_date = models.CharField(db_column='Agreed_Implementation_Date', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     revised_implementation_date = models.CharField(db_column='Revised_Implementation_Date', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     last_status_update = models.CharField(db_column='Last_Status_Update', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     ageing_days = models.CharField(db_column='Ageing__Days', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
#     actual_implementation_date = models.CharField(db_column='Actual_Implementation_Date', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     owner = models.CharField(db_column='Owner', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     final_approver =models.ForeignKey(Dept, on_delete=models.CASCADE) # Field name made lowercase.


