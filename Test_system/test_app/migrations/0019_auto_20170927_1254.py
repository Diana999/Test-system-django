# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-27 09:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0018_auto_20170926_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 9, 27, 9, 54, 27, 379746, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 9, 27, 9, 54, 27, 380965, tzinfo=utc), null=True),
        ),
        migrations.RemoveField(
            model_name='review',
            name='tests',
        ),
        migrations.AddField(
            model_name='review',
            name='tests',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='test_app.Test'),
        ),
        migrations.AlterField(
            model_name='test',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 9, 27, 9, 54, 27, 376218, tzinfo=utc), null=True),
        ),
    ]
