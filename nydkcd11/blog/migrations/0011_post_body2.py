# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 13:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20170628_0334'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body2',
            field=models.TextField(default=django.utils.timezone.now, verbose_name=b'Main Body of Text'),
            preserve_default=False,
        ),
    ]