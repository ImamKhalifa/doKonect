# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-16 14:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_auto_20170916_1432'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patientvisit',
            options={'ordering': ['-date']},
        ),
    ]
