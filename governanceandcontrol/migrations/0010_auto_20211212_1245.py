# Generated by Django 2.2.12 on 2021-12-12 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('governanceandcontrol', '0009_auto_20211209_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gnctable',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='governanceandcontrol.Dept'),
            preserve_default=False,
        ),
    ]
