# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-22 15:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0027_upcomingevent_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='upcomingevent',
            old_name='image',
            new_name='images',
        ),
    ]