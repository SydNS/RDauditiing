from django.db import models

# Create your models here.


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

