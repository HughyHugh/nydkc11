# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-19 00:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20170818_2238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='def_short',
        ),
        migrations.RemoveField(
            model_name='level',
            name='extend_desc',
        ),
    ]
