# Generated by Django 4.0 on 2022-02-12 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riskmanagement', '0007_alter_riskmanagement_risk_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riskmanagement',
            name='control_description',
            field=models.TextField(blank=True, db_column='Control_Description', max_length=100, null=True),
        ),
    ]
