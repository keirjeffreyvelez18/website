# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-10 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0042_auto_20180410_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researchtitle',
            name='research_year',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
