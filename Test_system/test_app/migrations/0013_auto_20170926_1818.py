# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-26 15:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0012_auto_20170926_0038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_date', models.DateTimeField(blank=True, default=datetime.datetime(2017, 9, 26, 15, 18, 57, 740257, tzinfo=utc), null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='applications',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 9, 26, 15, 18, 57, 738052, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 9, 26, 15, 18, 57, 735253, tzinfo=utc), null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='group',
            field=models.ManyToManyField(blank=True, default='', to='test_app.Test'),
        ),
    ]
