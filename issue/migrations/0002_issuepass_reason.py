# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-23 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuepass',
            name='reason',
            field=models.TextField(null=True),
        ),
    ]
