# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-19 13:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0016_auto_20170919_1330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientvisit',
            name='user_id',
        ),
    ]
