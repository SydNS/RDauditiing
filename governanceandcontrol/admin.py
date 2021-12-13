from django.contrib import admin
from . import models

# Register your models here.
from .models import GncTable, Dept, Person, GradingUser
from .models import RiskManagement

admin.site.site_header = 'Ruth Doreen Auditing Tool'


# admin.site.register(RiskManagement)
# admin.site.register(GncTable)


# class Dept(models.Model):
#     CRITICALITY_LEVELS = (
#         ('low', 'low'),
#         ('medium', 'medium'),
#         ('high', 'high'),
#     )
#     deptname = models.TextField()
#     deptrole = models.TextField()
#     deptcriticality = models.TextField()
#     numberofmembers = models.IntegerField()
#     criticality = models.CharField(db_column='Criticality', max_length=20, blank=False, null=True,
#                                    choices=CRITICALITY_LEVELS, default='draft')  # Field name made lowercase.

@admin.register(Dept)
class DeptAdmin(admin.ModelAdmin):
    list_display = ('deptname', 'deptrole', 'numberofmembers', 'criticality',)
    list_filter = ('deptname', 'deptrole',  'numberofmembers', 'criticality',)
    search_fields = ('deptname', 'deptrole', 'numberofmembers', 'criticality',)


# class Person(models.Model):
#     last_name = models.TextField()
#     first_name = models.TextField()
#     personemail = models.EmailField()
#     personsdept = models.ForeignKey(Dept, on_delete=models.CASCADE)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'personemail', 'personsdept',)
    list_filter = ('last_name', 'first_name', 'personemail', 'personsdept',)
    search_fields = ('last_name', 'first_name', 'personemail', 'personsdept',)


#
# class GradingUser(models.Model):
#     person = models.ForeignKey(Person, on_delete=models.CASCADE)
#     grade = models.PositiveSmallIntegerField()
#     deptnem = models.ForeignKey(Dept, on_delete=models.CASCADE)
#
@admin.register(GradingUser)
class GradingUserAdmin(admin.ModelAdmin):
    list_display = ('person', 'grade', 'deptnem',)
    list_filter = ('person', 'grade', 'deptnem',)
    search_fields = ('person', 'grade', 'deptnem',)


@admin.register(GncTable)
class GncTableAdmin(admin.ModelAdmin):
    list_display = ('audit_project_code', 'audit_project_name', 'quarter', 'audit_project_type',
                    'issue_title', 'criticality', 'root_cause_analysis', 'recommendation',
                    'action_plan', 'recommendation_state', 'agreed_implementation_date', 'revised_implementation_date'
                    , 'last_status_update', 'ageing_days', 'actual_implementation_date', 'owner', 'final_approver',
                    )
    list_filter = ('audit_project_name', 'quarter',
                   'criticality',
                   )
    search_fields = ('audit_project_code', 'audit_project_name', 'quarter',
                     'criticality', 'owner',
                     )


#
# @admin.register(Auditorofauditors)
# class AuditorofauditorsAdmin(admin.ModelAdmin):
#     list_display = ('internal_audit_leading_practices', 'iia_standards', 'current_status_at_xy', 'assessment',
#                     'recommendations', 'action_plan', 'recommendation_state', 'agreed_implementation_date',
#                     'revised_implementation_date', 'last_status_update', 'ageing_days'
#                     , 'actual_implementation_date','owner', 'final_approver',
#                     )
#     list_filter = ('internal_audit_leading_practices','iia_standards', 'current_status_at_xy', 'ageing_days', )
#     search_fields = ('internal_audit_leading_practices', 'iia_standards', 'current_status_at_xy', 'assessment',
#                     'recommendations', 'action_plan', 'recommendation_state', 'agreed_implementation_date',
#                     'revised_implementation_date', 'last_status_update', 'ageing_days'
#                     , 'actual_implementation_date','owner', 'final_approver',
#                     )

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
