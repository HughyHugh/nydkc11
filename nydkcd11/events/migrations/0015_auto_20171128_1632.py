# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-28 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_auto_20170902_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convention',
            name='background_image',
            field=models.ImageField(upload_to='conventions'),
        ),
        migrations.AlterField(
            model_name='part',
            name='image',
            field=models.ImageField(upload_to='conventions'),
        ),
    ]