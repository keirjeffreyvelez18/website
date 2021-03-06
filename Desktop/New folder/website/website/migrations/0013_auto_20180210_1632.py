# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-10 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_auto_20180210_0118'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='outreachpost',
            options={'get_latest_by': 'outreach_date'},
        ),
        migrations.AddField(
            model_name='newspost',
            name='news_shortdesc',
            field=models.CharField(default='Short Description', help_text='Short Description for Preview text.', max_length=10000, null=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newspost',
            name='news_description',
            field=models.CharField(help_text='Full content', max_length=10000, null=''),
        ),
        migrations.AlterField(
            model_name='outreachpost',
            name='outreach_date',
            field=models.DateField(auto_now_add=True, null=''),
        ),
    ]
