# Generated by Django 2.2.1 on 2021-05-09 05:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyTime', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='time',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='日期'),
        ),
        migrations.AddField(
            model_name='time',
            name='planningTime',
            field=models.TimeField(default=datetime.datetime.now, verbose_name='计划时间'),
        ),
        migrations.AlterField(
            model_name='time',
            name='endTime',
            field=models.TimeField(default=datetime.datetime.now, verbose_name='结束时间'),
        ),
        migrations.AlterField(
            model_name='time',
            name='startTime',
            field=models.TimeField(default=datetime.datetime.now, verbose_name='开始时间'),
        ),
    ]
