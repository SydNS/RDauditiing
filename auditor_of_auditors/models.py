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
        ('DOES_NOT_CONFORMS', 'DOES_NOT_CONFORMS'),
    )
    IIA_STANDARDS = (
        ("The Purpose, Authority and Responsibility of the internal audit activit"
         "y should be formally defined in a charter, consistent with the definition o"
         "f internal auditing, the Code of Ethics, and the IIA standards. The CAE must pe"
         "riodically review the internal audit charter and present it to senior management "
         "and the board for approval. Interpretation – The internal audit charter is a "
         "formal document that defines the internal audit activity’s purpose, authority, an"
         "d responsibility. The charter establishes the internal audit activity’s position withi"
         "n the organisation, including the nature of the Chief Audit Executive’s functional report"
         "ing relationship with the board, authorizes access to records, personnel, and physical properti"
         "es relevant to the performance of engagements; and defines the scope of internal audit activities."
         " Final approval of the charter resides with the board.","IIA AS 1000"),
        ("(PS 1300)- QAIP The CAE must develop and maintain a quality assurance and improvement program that covers"
         " all aspects of the internal audit activity."
         "(PS 1310)- The QAIP must include both internal and external assessments.Interpretation:A "
         "quality assurance and improvement program is designed to enable an evaluation of the intern"
         "al audit activity’s conformance with the Definition of Internal Auditing and the Standards and "
         "an evaluation of whether internal auditors apply the Code of Ethics. The program also assesses the effi"
         "ciency and effectiveness of the internal audit activity and identifies opportunities for improvement.Ongoing"
         " monitoring is an integral part of the day-to-day supervision, review, and measurement of the internal audit activity."
         " Ongoing monitoring is incorporated into the routine policies and practices used to manage the internal audit activity "
         "and uses processes, tools, and information considered necessary to evaluate conformance with the Definition of Internal "
         "Auditing, the Core Principles, the Code of Ethics, and the Standards.","PS 1300- QAIP,  PS 1310"),
        ( "The chief audit executive must report periodically to senior management and the board on the internal audit activity’s purpose, authority, responsibility, and performance relative to its plan and on its conformance with the Code of Ethics and the Standards. Reporting must include significant risk and control issues, including fraud risks, governance issues, and other matters that require the attention of senior management and/or the board. Interpretation: The frequency and content of reporting are determined collaboratively by the chief audit executive, senior management, and the board. The frequency and content of reporting depends on the importance of the information to be communicated and the urgency of the related actions to be taken by senior management and/or the board. The chief audit executive’s reporting and communication to senior management and the board must include information about: • The audit charter. • Independence of the internal audit activity. • The audit plan and progress against the plan. • Resource requirements. • Results of audit activities. • Conformance with the Code of Ethics and the Standards, and action plans to address any significant conformance issues. • Management’s response to risk that, in the chief audit executive’s judgment, may be unacceptable to the organization.  ","2060 – Reporting to Senior Management and the Board "),
        ("IIA AS 1100: The IAD must be independent, and internal auditors must be objective in performing their work. (IIA AS 1110): The chief audit executive must report to a level within the organization that allows the internal audit activity to fulfill its responsibilities. The chief audit executive must confirm to the board, at least annually, the organizational independence of the internal audit activity. (IIA AS 1110.A1): The IAD must be free from interference in determining the scope of internal auditing, performing work, and communicating results ","IIA AS 1100, IIA AS 1110, IIA AS 1110.A1"),
        ("The CAE share information and coordinate activities with other internal and external providers of assurance and consulting services to ensure proper coverage and minimize duplication efforts.","IIA PS 2050"),
        ("(PS 1300)- QAIP The CAE must develop and maintain a quality assurance and improvement program that covers all aspects of the internal audit activity. (PS 1310)- The QAIP must include both internal and external assessments. Interpretation: A quality assurance and improvement program is designed to enable an evaluation of the internal audit activity’s conformance with the Definition of Internal Auditing and the Standards and an evaluation of whether internal auditors apply the Code of Ethics. The program also assesses the efficiency and effectiveness of the internal audit activity and identifies opportunities for improvement. Ongoing monitoring is an integral part of the day-to-day supervision, review, and measurement of the internal audit activity. Ongoing monitoring is incorporated into the routine policies and practices used to manage the internal audit activity and uses processes, tools, and information considered necessary to evaluate conformance with the Definition of Internal Auditing, the Core Principles, the Code of Ethics, and the Standards. ","PS 1300- QAIP,  PS 1310"),
        ("(IIA PS 2020): The chief audit executive must communicate the internal audit activity's plans and resource requirements, including significant interim changes, to senior management and the board for review and approval. The chief audit executive must also communicate the impact of resource limitations. (IIA PS 2010): The chief audit executive must establish risk-based plans to determine the priorities of the internal audit activity, consistent with the organization's goals. (IIA PS 2010.A1): The internal audit activity's plan of engagements must be based on a documented risk assessment, undertaken at least annually. The input of senior management and the board must be considered in this process. (IIA PS 2010.A2): The Chief Audit Executive must identify and consider the expectations of senior management, the board, and other stakeholders for internal audit opinions and other conclusions. (IIA 2030): The chief audit executive must ensure that internal audit resources are appropriate, sufficient, and effectively deployed to achieve the approved plan. (IIA PS 2100): The internal audit activity must evaluate and contribute to the improvement of governance, risk management, and control processes using a systematic and disciplined approach. (IIA PS 2120) The internal audit activity must evaluate the effectiveness and contribute to the improvement of risk management processes. (IIA PS 2130) The internal audit activity must assist the organization in maintaining effective controls in responding to risks within the organization’s governance, operations, and information systems. ","IIA PS 2020, IIA PS 2010 , IIA PS 2010.A1, IIA PS 2010.A2, IIA  2030, IIA PS 2100, IIA PS 2120, IIA PS 2130. ")
        ,("(IIA PS 2200) Internal auditors must develop and document a plan for each engagement, including the engagement’s objectives, scope, timing, and resource allocation. (IIA PS 2201) in planning the engagement, internal auditors must consider: • The objectives of the activity being reviewed and the means by which the activity controls its performance. • The significant risks to the activity, its objectives, resources, and operations and the means by which the potential impact of risk is kept to an acceptable level. • The adequacy and effectiveness of the activity’s governance, risk management, and control processes compared to a relevant framework or model and • The opportunities for making significant improvements to the activity’s governance, risk management and control processes.","IIA PS 2300, IIA PS 2330 "),
        ("(IIA PS 2300) Internal auditors must identify, analyze, evaluate, and document sufficient information to achieve the engagement objectives. Interpretation: Sufficient information is factual, adequate, and convincing so that a prudent, informed person would reach the same conclusions as the auditor. Reliable information is the best attainable information through the use of appropriate engagement techniques. Relevant information supports engagement observations and recommendations and is consistent with the objectives for the engagement. (IIA PS 2330) Internal auditors must document relevant information to support the conclusions and engagement results.","IIA PS 2300, IIA PS 2330"),
        ("(IIA PS 2340) Engagements must be properly supervised to ensure objectives are achieved, quality is assured, and staff are developed. Interpretation: The extent of supervision will depend on the proficiency and experience of internal auditors and the complexity of the engagement. The Chief Audit Executive has the overall responsibility for supervising the engagement, whether by or for the internal audit activity, but may designate appropriately experienced members of the internal audit activity to perform the review. Appropriate evidence of supervision is documented and retained. ","IIA PS 2340")
    )
    internal_audit_leading_practices = models.TextField(db_column='Internal_audit_leading_Practices', max_length=100, blank=True, null=True)  # Field name made lowercase.
    iia_standards = models.TextField(choices=IIA_STANDARDS,db_column='IIA_Standards', max_length=100, blank=False, null=True)  # Field name made lowercase.
    current_status_at_xy = models.CharField(choices=CURRENT_STATUS_XY,db_column='Current_Status_at_XY', max_length=100, blank=False, null=True)  # Field name made lowercase.
    assessment = models.CharField(choices=ASSESSMENT,db_column='Assessment', max_length=100, blank=False, null=True)  # Field name made lowercase.
    recommendations = models.TextField(db_column='Recommendations', max_length=500, blank=True, null=True)  # Field name made lowercase.
    action_plan = models.TextField(db_column='Action_Plan', max_length=500, blank=True, null=True)  # Field name made lowercase.
    recommendation_state = models.CharField(choices=CURRENT_STATUS_XY,db_column='Recommendation_State', max_length=100, blank=False, null=True)  # Field name made lowercase.
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



