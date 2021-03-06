# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-26 19:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0017_auto_20170926_2239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='groups',
            new_name='tests',
        ),
        migrations.AlterField(
            model_name='applications',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 9, 26, 19, 53, 40, 803239, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 9, 26, 19, 53, 40, 804795, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 9, 26, 19, 53, 40, 799316, tzinfo=utc), null=True),
        ),
    ]
