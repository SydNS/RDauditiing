from django.db import models

class Dept(models.Model):
    CRITICALITY_LEVELS = (
        ('low', 'low'),
        ('medium', 'medium'),
        ('high', 'high'),
    )
    deptname = models.CharField(max_length=100)
    deptrole = models.CharField(max_length=100)
    numberofmembers = models.IntegerField()
    criticality = models.CharField(db_column='Criticality', max_length=20, blank=False, null=True,
                                   choices=CRITICALITY_LEVELS, default='draft')  # Field name made lowercase.
    def __str__(self):
        return self.deptname


    # class Meta:
    #     unique_together = ("deptname", "deptrole",)


class Person(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    personemail = models.EmailField()
    personsdept = models.ForeignKey(Dept, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "People"

    def __str__(self):
        return self.last_name


class GradingUser(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    grade = models.PositiveSmallIntegerField()
    deptnem = models.ForeignKey(Dept, on_delete=models.CASCADE)


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
    audit_project_code = models.CharField(db_column='Audit_Project_Code', max_length=100, blank=False,
                                          null=True)  # Field name made lowercase.
    audit_project_name = models.CharField(db_column='Audit_Project_Name', max_length=100, blank=False,
                                          null=True)  # Field name made lowercase.
    quarter = models.CharField(db_column='Quarter', choices=QUARTERS, max_length=100, blank=False,
                               null=True)  # Field name made lowercase.
    audit_project_type = models.CharField(db_column='Audit_Project_Type', max_length=100, blank=True,choices=PROJECT_TYPE,
                                          null=True)  # Field name made lowercase.
    issue_title = models.CharField(db_column='Issue_Title', max_length=50, blank=False,
                                   null=True)  # Field name made lowercase.
    criticality = models.CharField(db_column='Criticality', max_length=20, blank=False, null=True,
                                   choices=CRITICAL_LEVELS, default='draft')  # Field name made lowercase.
    root_cause_analysis = models.CharField(db_column='Root_Cause_Analysis', choices=ROOT_CAUSE_ANALYSIS, max_length=100,
                                           blank=False, null=True)  # Field name made lowercase.
    recommendation = models.CharField(db_column='Recommendation', max_length=100, blank=False,

                                      null=True)  # Field name made lowercase.
    action_plan = models.CharField(db_column='Action_Plan', max_length=100, blank=False,
                                   null=True)  # Field name made lowercase.
    recommendation_state = models.CharField(db_column='Recommendation_State', max_length=100, blank=False, choices=RECOMMENDATION_STATE,
                                            null=True)  # Field name made lowercase.
    agreed_implementation_date = models.DateField(db_column='Agreed_Implementation_Date', max_length=100, blank=True,
                                                  null=True)  # Field name made lowercase.
    revised_implementation_date = models.DateField(db_column='Revised_Implementation_Date', max_length=100, blank=True,
                                                   null=True)  # Field name made lowercase.
    last_status_update = models.DateField(db_column='Last_Status_Update', max_length=100, blank=False,
                                          null=True)  # Field name made lowercase.
    ageing_days = models.FloatField(db_column='Ageing__Days', max_length=10, blank=False,
                                    null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    actual_implementation_date = models.DateField(db_column='Actual_Implementation_Date', max_length=100, blank=True,
                                                  null=True)  # Field name made lowercase.
    owner = models.CharField(db_column='Owner', max_length=100, blank=True, null=True)    # Field name made lowercase.
    final_approver = models.ForeignKey(Person, on_delete=models.CASCADE)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'GncTable'
    def __str__(self):
        return self.audit_project_name


class RiskManagement(models.Model):
    IMPACT_LEVELS = (
        ('low', 'low'),
        ('moderate', 'moderate'),
        ('high', 'high'),
    )
    RATE_LEVELS = (
        ('low', 'low'),
        ('moderate', 'moderate'),
        ('high', 'high'),
    )
    LIKELIHOOD = (
        ('low', 'low'),
        ('moderate', 'moderate'),
        ('high', 'high'),
    )
    CONTROL_EXISTANCE = (
        ('yes', 'yes'),
        ('no', 'no'),
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
    # Financial - Liquidity, Financial - Interest
    # Rate, Financial - Foreign
    # Exchange, Financial - Investment, Financial - Market, Operational - Transaction, Operational - Human
    # Resources, Operational - ICT, operational - Fraud, Legal, Compliance, Strategic, Reputation, Governance, Other

    RISK_CATEGORY = (
        ('Financial_Liquidity', 'Financial_Liquidity'),
        ('Financial_Interest_Rate', 'Financial_Interest_Rate'),
        ('Financial_Foreign_Exchange', 'Financial_Foreign_Exchange'),
        ('Financial_Investment', 'Financial_Investment'),
        ('Financial_Market', 'Financial_Market'),
        ('Operational_Transaction', 'Operational_Transaction'),
        ('Operational_Human_Resources', 'Operational_Human_Resources'),
        ('Operational_ICT', 'Operational_ICT'),
        ('Operational_Fraud', 'Operational_Fraud'),
        ('Legal', 'Legal'),
        ('Compliance', 'Compliance'),
        ('Strategic', 'Strategic'),
        ('Reputation', 'Reputation'),
        ('Governance', 'Governance'),
        ('Other', 'Other'),
    )

    xy_strategic_pillar = models.CharField(db_column='XY_Strategic_Pillar', max_length=100, blank=True,
                                           null=True)  # Field name made lowercase.
    xy_strategic_objectives = models.CharField(db_column='XY_Strategic_Objectives', max_length=100, blank=True,
                                               null=True)  # Field name made lowercase.
    risk_category = models.CharField(db_column='Risk_Category', max_length=100, blank=True,choices=RISK_CATEGORY,
                                     null=True)  # Field name made lowercase.
    risk_description = models.CharField(db_column='Risk_Description', max_length=100, blank=True,
                                        null=True)  # Field name made lowercase.
    likelihood = models.CharField(db_column='Likelihood', max_length=100, blank=True,choices=LIKELIHOOD,
                                  null=True)  # Field name made lowercase.
    impact = models.CharField(db_column='Impact', max_length=100, blank=True, null=True,choices=IMPACT_LEVELS)  # Field name made lowercase.
    risk_rating = models.CharField(db_column='Risk_Rating', max_length=100, blank=True,choices=RATE_LEVELS,
                                   null=True)  # Field name made lowercase.
    control_exists_yesno = models.CharField(db_column='Control_Exists_YesNo', max_length=100, blank=True,choices=CONTROL_EXISTANCE,
                                            null=True)  # Field name made lowercase.
    control_description = models.CharField(db_column='Control_Description', max_length=100, blank=True,
                                           null=True)  # Field name made lowercase.
    control_is_adequate_yesno = models.CharField(db_column='Control_is_Adequate_YesNo', max_length=100, blank=True
                                                 ,choices=CONTROL_EXISTANCE,
                                                 null=True)  # Field name made lowercase.
    recommended_control = models.CharField(db_column='Recommended_Control', max_length=100, blank=True,
                                           null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kri = models.CharField(db_column='KRI', max_length=100, blank=True, null=True)  # Field name made lowercase.
    target = models.CharField(db_column='Target', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE) # Field name made lowercase.

    def __str__(self):
        return self.xy_strategic_pillar


#     class Meta:
#         managed = False
#         db_table = 'Risk_Management'


class Auditorofauditors(models.Model):
    internal_audit_leading_practices = models.CharField(db_column='Internal_audit_leading_Practices', max_length=100, blank=True, null=True)  # Field name made lowercase.
    iia_standards = models.CharField(db_column='IIA_Standards', max_length=100, blank=True, null=True)  # Field name made lowercase.
    current_status_at_xy = models.CharField(db_column='Current_Status_at_XY', max_length=100, blank=True, null=True)  # Field name made lowercase.
    assessment = models.CharField(db_column='Assessment', max_length=100, blank=True, null=True)  # Field name made lowercase.
    recommendations = models.CharField(db_column='Recommendations', max_length=100, blank=True, null=True)  # Field name made lowercase.
    action_plan = models.CharField(db_column='Action_Plan', max_length=100, blank=True, null=True)  # Field name made lowercase.
    recommendation_state = models.CharField(db_column='Recommendation_State', max_length=100, blank=True, null=True)  # Field name made lowercase.
    agreed_implementation_date = models.CharField(db_column='Agreed_Implementation_Date', max_length=100, blank=True, null=True)  # Field name made lowercase.
    revised_implementation_date = models.CharField(db_column='Revised_Implementation_Date', max_length=100, blank=True, null=True)  # Field name made lowercase.
    last_status_update = models.CharField(db_column='Last_Status_Update', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ageing_days = models.CharField(db_column='Ageing__Days', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    actual_implementation_date = models.CharField(db_column='Actual_Implementation_Date', max_length=100, blank=True, null=True)  # Field name made lowercase.
    owner = models.CharField(db_column='Owner', max_length=100, blank=True, null=True)  # Field name made lowercase.
    final_approver =models.ForeignKey(Dept, on_delete=models.CASCADE) # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'AuditorOfAuditors'from django.db import models

