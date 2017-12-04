# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 22:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0004_minutes_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='minutes',
            name='url',
        ),
        migrations.AddField(
            model_name='minutes',
            name='notes',
            field=models.FileField(default=django.utils.timezone.now, upload_to=b'minutes/'),
            preserve_default=False,
        ),
    ]