# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-12 13:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0051_researchtitle_research_program'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='researchtitle',
            name='research_year',
        ),
    ]
