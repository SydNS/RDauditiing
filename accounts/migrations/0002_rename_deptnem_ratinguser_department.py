# Generated by Django 4.0 on 2022-02-09 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ratinguser',
            old_name='deptnem',
            new_name='department',
        ),
    ]