# Generated by Django 4.0 on 2022-02-09 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_ratinguser_rate_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratinguser',
            name='rate_level',
            field=models.IntegerField(choices=[(1, '1 of 10'), (2, '2 of 10'), (3, '3 of 10'), (4, '4 of 10'), (5, '5 of 10'), (6, '6 of 10'), (7, '7 of 10'), (8, '8 of 10'), (9, '9 of 10'), (10, '10 of 10')]),
        ),
    ]