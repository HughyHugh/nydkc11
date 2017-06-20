# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-20 15:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_faq'),
    ]

    operations = [
        migrations.AddField(
            model_name='division',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
    ]
