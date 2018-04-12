# Generated by Django 2.0.2 on 2018-03-02 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_delete_research'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='alumni_url',
            field=models.URLField(default='http://www.google.com/', help_text='LinkedIn / Professional Website of the Alumni', null=''),
            preserve_default=False,
        ),
    ]
