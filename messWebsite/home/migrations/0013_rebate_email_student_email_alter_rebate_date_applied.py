# Generated by Django 4.1.7 on 2023-04-16 21:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_rebate_date_applied'),
    ]

    operations = [
        migrations.AddField(
            model_name='rebate',
            name='email',
            field=models.CharField(default=0, max_length=30),
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='rebate',
            name='date_applied',
            field=models.DateField(default=datetime.date(2023, 4, 17), help_text='Date on which the rebate was applied'),
        ),
    ]
