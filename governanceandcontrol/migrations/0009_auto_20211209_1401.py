# Generated by Django 2.2.12 on 2021-12-09 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('governanceandcontrol', '0008_auto_20211209_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditorofauditors',
            name='final_approver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='governanceandcontrol.Person'),
        ),
    ]
