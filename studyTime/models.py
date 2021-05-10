from django.db import models
from datetime import datetime

# Create your models here.


class Time(models.Model):
    title = models.CharField(max_length=20, verbose_name=u'学习主题')
    date = models.DateTimeField(default=datetime.now, verbose_name=u'日期')
    startTime = models.TimeField(default=datetime.now, verbose_name=u'开始时间')
    planningTime = models.TimeField(default=datetime.now, verbose_name=u'计划时间')
    endTime = models.TimeField(default=datetime.now, verbose_name=u'结束时间')

    def __str__(self):
        return self.title
