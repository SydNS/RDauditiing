# Generated by Django 2.2.12 on 2021-12-09 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('governanceandcontrol', '0007_auto_20211209_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditorofauditors',
            name='ageing_days',
            field=models.FloatField(blank=True, db_column='Ageing__Days', max_length=100, null=True),
        ),
    ]