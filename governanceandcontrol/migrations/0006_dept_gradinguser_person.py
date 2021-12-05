# Generated by Django 2.2.12 on 2021-12-04 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('governanceandcontrol', '0005_auto_20211202_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptname', models.TextField()),
                ('deptrole', models.TextField()),
                ('deptcriticality', models.TextField()),
                ('numberofmembers', models.IntegerField()),
                ('criticality', models.CharField(choices=[('low', 'low'), ('medium', 'medium'), ('high', 'high')], db_column='Criticality', default='draft', max_length=20, null=True)),
            ],
            options={
                'unique_together': {('deptname', 'deptrole')},
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.TextField()),
                ('first_name', models.TextField()),
                ('personemail', models.EmailField(max_length=254)),
                ('personsdept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='governanceandcontrol.Dept')),
            ],
            options={
                'verbose_name_plural': 'People',
            },
        ),
        migrations.CreateModel(
            name='GradingUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.PositiveSmallIntegerField()),
                ('deptnem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='governanceandcontrol.Dept')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='governanceandcontrol.Person')),
            ],
        ),
    ]