# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-23 10:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0002_issuepass_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approvepass',
            name='real_outTime',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 23, 16, 22, 14, 682403)),
        ),
    ]
