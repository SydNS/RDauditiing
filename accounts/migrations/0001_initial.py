# Generated by Django 4.0 on 2022-02-13 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date_joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last_login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('hide_email', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departmentname', models.CharField(max_length=100)),
                ('departmentrole', models.CharField(max_length=100)),
                ('numberofmembers', models.IntegerField()),
                ('criticality', models.CharField(choices=[('low', 'low'), ('medium', 'medium'), ('high', 'high')], db_column='Criticality', default='Low', max_length=20, null=True)),
            ],
            options={
                'unique_together': {('departmentname',)},
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='profileimages/')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=6)),
                ('address', models.CharField(max_length=100)),
                ('name_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
                ('personsdept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.department')),
            ],
            options={
                'verbose_name_plural': 'People',
            },
        ),
        migrations.CreateModel(
            name='RatingUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate_level', models.IntegerField(choices=[(1, '1 of 10'), (2, '2 of 10'), (3, '3 of 10'), (4, '4 of 10'), (5, '5 of 10'), (6, '6 of 10'), (7, '7 of 10'), (8, '8 of 10'), (9, '9 of 10'), (10, '10 of 10')])),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.department')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.person', unique=True)),
            ],
            options={
                'verbose_name_plural': 'Ratings',
            },
        ),
    ]
