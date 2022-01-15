from django.db import models



class GncTable(models.Model):
    CRITICAL_LEVELS = (
        ('low', 'low'),
        ('medium', 'medium'),
        ('high', 'high'),
    )
    QUARTERS = (
        ('Q1', 'Q1'),
        ('Q2', 'Q2'),
        ('Q3', 'Q3'),
        ('Q4', 'Q4'),
    )
    ROOT_CAUSE_ANALYSIS = (
        ('POCESSES', 'POCESSES'),
        ('PEOPLE', 'PEOPLE'),
        ('TECHNOLOGY', 'TECHNOLOGY'),
    )
    RECOMMENDATION_STATE = (
        ('PARTIALLY_IMPLEMENTED', 'PARTIALLY_IMPLEMENTED'),
        ('PENDING', 'PENDING'),
        ('CLOSED', 'CLOSED'),
    )

    PROJECT_TYPE = (
        ('Business', 'Business'),
        ('ICT', 'ICT'),
        ('Corporate Affairs', 'Corporate Affairs'),
    )
    
    audit_project_code = models.CharField(db_column='Audit_Project_Code', max_length=100, blank=False,null=True)  # Field name made lowercase.
    audit_project_name = models.CharField(db_column='Audit_Project_Name', max_length=100, blank=False,null=True)  # Field name made lowercase.
    quarter = models.CharField(db_column='Quarter', choices=QUARTERS, max_length=100, blank=False,null=True)  # Field name made lowercase.
    audit_project_type = models.CharField(db_column='Audit_Project_Type', max_length=100, blank=True,choices=PROJECT_TYPE,null=True)  # Field name made lowercase.
    issue_title = models.CharField(db_column='Issue_Title', max_length=50, blank=False,null=True)  # Field name made lowercase.
    criticality = models.CharField(db_column='Criticality', max_length=20, blank=False, null=True,choices=CRITICAL_LEVELS, default='draft')  # Field name made lowercase.
    root_cause_analysis = models.CharField(db_column='Root_Cause_Analysis', choices=ROOT_CAUSE_ANALYSIS, max_length=100,blank=False, null=True)  # Field name made lowercase.
    recommendation = models.CharField(db_column='Recommendation', max_length=100, blank=False,null=True)  # Field name made lowercase.
    action_plan = models.CharField(db_column='Action_Plan', max_length=100, blank=False,null=True)  # Field name made lowercase.
    recommendation_state = models.CharField(db_column='Recommendation_State', max_length=100, blank=False, choices=RECOMMENDATION_STATE,null=True)  # Field name made lowercase.
    agreed_implementation_date = models.DateField(db_column='Agreed_Implementation_Date', max_length=100, blank=True,null=True)  # Field name made lowercase.
    revised_implementation_date = models.DateField(db_column='Revised_Implementation_Date', max_length=100, blank=True,null=True)  # Field name made lowercase.
    last_status_update = models.DateField(db_column='Last_Status_Update', max_length=100, blank=False,null=True)  # Field name made lowercase.
    ageing_days = models.FloatField(db_column='Ageing__Days', max_length=10, blank=False,null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    actual_implementation_date = models.DateField(db_column='Actual_Implementation_Date', max_length=100, blank=True,null=True)  # Field name made lowercase.
    owner = models.ForeignKey('accounts.Dept', on_delete=models.CASCADE)     # Field name made lowercase.
    final_approver = models.ForeignKey('accounts.Person', on_delete=models.CASCADE)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'GncTable'
    #       verbose_name_plural = "Governance & Control" /o add pluralise
    def __str__(self):
        return self.audit_project_name


