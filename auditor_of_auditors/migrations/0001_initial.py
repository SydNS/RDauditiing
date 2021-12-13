# Generated by Django 4.0 on 2021-12-13 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('governanceandcontrol', '0011_alter_dept_id_alter_gnctable_id_alter_gradinguser_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auditorofauditors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internal_audit_leading_practices', models.CharField(blank=True, db_column='Internal_audit_leading_Practices', max_length=100, null=True)),
                ('iia_standards', models.CharField(blank=True, db_column='IIA_Standards', max_length=100, null=True)),
                ('current_status_at_xy', models.CharField(blank=True, choices=[('PARTIALLY_IMPLEMENTED', 'PARTIALLY_IMPLEMENTED'), ('PENDING', 'PENDING'), ('CLOSED', 'CLOSED')], db_column='Current_Status_at_XY', max_length=100, null=True)),
                ('assessment', models.CharField(blank=True, db_column='Assessment', max_length=100, null=True)),
                ('recommendations', models.CharField(blank=True, db_column='Recommendations', max_length=100, null=True)),
                ('action_plan', models.CharField(blank=True, db_column='Action_Plan', max_length=100, null=True)),
                ('recommendation_state', models.CharField(blank=True, choices=[('PARTIALLY_IMPLEMENTED', 'PARTIALLY_IMPLEMENTED'), ('PENDING', 'PENDING'), ('CLOSED', 'CLOSED')], db_column='Recommendation_State', max_length=100, null=True)),
                ('agreed_implementation_date', models.DateField(blank=True, db_column='Agreed_Implementation_Date', max_length=100, null=True)),
                ('revised_implementation_date', models.DateField(blank=True, db_column='Revised_Implementation_Date', max_length=100, null=True)),
                ('last_status_update', models.CharField(blank=True, db_column='Last_Status_Update', max_length=100, null=True)),
                ('ageing_days', models.FloatField(blank=True, db_column='Ageing__Days', max_length=100, null=True)),
                ('actual_implementation_date', models.DateField(blank=True, db_column='Actual_Implementation_Date', max_length=100, null=True)),
                ('owner', models.CharField(blank=True, db_column='Owner', max_length=100, null=True)),
                ('final_approver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='governanceandcontrol.person')),
            ],
        ),
    ]
