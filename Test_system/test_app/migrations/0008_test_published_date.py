# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-25 12:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0007_auto_20170925_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 9, 25, 12, 57, 9, 427685, tzinfo=utc), null=True),
        ),
    ]