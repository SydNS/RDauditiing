# Generated by Django 2.2.12 on 2021-12-09 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('governanceandcontrol', '0003_auto_20211209_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gnctable',
            name='audit_project_type',
            field=models.CharField(blank=True, choices=[('Business', 'Business'), ('ICT', 'ICT'), ('Corporate Affairs', 'Corporate Affairs')], db_column='Audit_Project_Type', max_length=100, null=True),
        ),
    ]
