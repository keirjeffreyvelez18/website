# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-22 14:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0025_auto_20180322_2229'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='outreachpost',
            options={'get_latest_by': 'date'},
        ),
    ]
