# Generated by Django 2.2.1 on 2021-05-09 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='学习主题')),
                ('startTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('endTime', models.DateTimeField(auto_now_add=True, verbose_name='结束时间')),
            ],
        ),
    ]
