# Generated by Django 4.0 on 2021-12-13 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_account_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptname', models.CharField(max_length=100)),
                ('deptrole', models.CharField(max_length=100)),
                ('numberofmembers', models.IntegerField()),
                ('criticality', models.CharField(choices=[('low', 'low'), ('medium', 'medium'), ('high', 'high')], db_column='Criticality', default='draft', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('personemail', models.EmailField(max_length=254)),
                ('personsdept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.dept')),
            ],
            options={
                'verbose_name_plural': 'People',
            },
        ),
        migrations.CreateModel(
            name='GradingUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.PositiveSmallIntegerField()),
                ('deptnem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.dept')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.person')),
            ],
        ),
    ]
