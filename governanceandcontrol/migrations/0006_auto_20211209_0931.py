# Generated by Django 2.2.12 on 2021-12-09 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('governanceandcontrol', '0005_auto_20211209_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riskmanagement',
            name='likelihood',
            field=models.CharField(blank=True, choices=[('low', 'low'), ('moderate', 'moderate'), ('high', 'high')], db_column='Likelihood', max_length=100, null=True),
        ),
    ]