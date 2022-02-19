from django.db import models

# Create your models here.
# from AuditProject import governanceandcontrol

class Auditor_of_auditors(models.Model):
    CURRENT_STATUS_XY = (
        ('PARTIALLY_IMPLEMENTED', 'PARTIALLY_IMPLEMENTED'),
        ('PENDING', 'PENDING'),
        ('CLOSED', 'CLOSED'),
    )
    ASSESSMENT = (
        ('GENERALLY_CONFORMS', 'GENERALLY_CONFORMS'),
        ('PARTIALLY_CONFORMS', 'PARTIALLY_CONFORMS'),
        ('DOES_NOT_CONFORMS', 'GENERALLY_CONFORMS'),
    )
    internal_audit_leading_practices = models.CharField(db_column='Internal_audit_leading_Practices', max_length=100, blank=True, null=True)  # Field name made lowercase.
    iia_standards = models.CharField(db_column='IIA_Standards', max_length=100, blank=True, null=True)  # Field name made lowercase.
    current_status_at_xy = models.CharField(choices=CURRENT_STATUS_XY,db_column='Current_Status_at_XY', max_length=100, blank=True, null=True)  # Field name made lowercase.
    assessment = models.CharField(choices=ASSESSMENT,db_column='Assessment', max_length=100, blank=True, null=True)  # Field name made lowercase.
    recommendations = models.CharField(db_column='Recommendations', max_length=100, blank=True, null=True)  # Field name made lowercase.
    action_plan = models.CharField(db_column='Action_Plan', max_length=100, blank=True, null=True)  # Field name made lowercase.
    recommendation_state = models.CharField(choices=CURRENT_STATUS_XY,db_column='Recommendation_State', max_length=100, blank=True, null=True)  # Field name made lowercase.
    agreed_implementation_date = models.DateField(db_column='Agreed_Implementation_Date', max_length=100, blank=True, null=True)  # Field name made lowercase.
    revised_implementation_date = models.DateField(db_column='Revised_Implementation_Date', max_length=100, blank=True, null=True)  # Field name made lowercase.
    last_status_update = models.CharField(db_column='Last_Status_Update', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ageing_days = models.FloatField(db_column='Ageing__Days', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    actual_implementation_date = models.DateField(db_column='Actual_Implementation_Date', max_length=100, blank=True, null=True)  # Field name made lowercase.
    # owner = models.CharField(db_column='Owner', max_length=100, blank=True, null=True)  # Field name made lowercase.
    owner = models.ForeignKey('accounts.Department', on_delete=models.CASCADE)     # Field name made lowercase.
    final_approver =models.ForeignKey('accounts.Person', on_delete=models.CASCADE) # Field name made lowercase.

    def __str__(self):
        return self.internal_audit_leading_practices

    class Meta:
        verbose_name_plural = "Auditor of auditors"



