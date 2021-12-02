from django.contrib import admin
from . import models

# Register your models here.
from .models import GncTable
from .models import RiskManagement

admin.site.site_header = 'Ruth Doreen Auditing Tool'


# admin.site.register(RiskManagement)
# admin.site.register(GncTable)


@admin.register(GncTable)
class GncTableAdmin(admin.ModelAdmin):
    list_display = ('audit_project_code', 'audit_project_name', 'quarter', 'audit_project_type',
                    'issue_title', 'criticality', 'root_cause_analysis', 'recommendation',
                    'action_plan', 'recommendation_state', 'agreed_implementation_date', 'revised_implementation_date'
                    , 'last_status_update', 'ageing_days', 'actual_implementation_date', 'owner', 'final_approver',
                    )
    list_filter = ('audit_project_code', 'audit_project_name', 'quarter',
                   'criticality', 'owner',
                   )
    search_fields = ('audit_project_code', 'audit_project_name', 'quarter',
                     'criticality', 'owner',
                     )
    # prepopulated_fields = {'criticality': ('low', 'medium', 'high')}
    # raw_id_fields = ('author',)
    # date_hierarchy = 'publish'
    # ordering = ('status', 'publish')

# class RiskManagement(models.Model):
#     xy_strategic_pillar = models.CharField(db_column='XY_Strategic_Pillar', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     xy_strategic_objectives = models.CharField(db_column='XY_Strategic_Objectives', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     risk_category = models.CharField(db_column='Risk_Category', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     risk_description = models.CharField(db_column='Risk_Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     likelihood = models.CharField(db_column='Likelihood', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     impact = models.CharField(db_column='Impact', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     risk_rating = models.CharField(db_column='Risk_Rating', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     control_exists_yesno = models.CharField(db_column='Control_Exists_YesNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     control_description = models.CharField(db_column='Control_Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     control_is_adequate_yesno = models.CharField(db_column='Control_is_Adequate_YesNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     recommended_control = models.CharField(db_column='Recommended_Control', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     action = models.CharField(db_column='Action', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     kri = models.CharField(db_column='KRI', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     target = models.CharField(db_column='Target', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     dept = models.CharField(db_column='Dept', max_length=100, blank=True, null=True)  # Field name made lowercase.
