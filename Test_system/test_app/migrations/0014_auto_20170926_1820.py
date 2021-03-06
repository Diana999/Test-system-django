# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-26 15:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0013_auto_20170926_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 9, 26, 15, 20, 54, 473796, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 9, 26, 15, 20, 54, 475807, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 9, 26, 15, 20, 54, 470398, tzinfo=utc), null=True),
        ),
    ]
