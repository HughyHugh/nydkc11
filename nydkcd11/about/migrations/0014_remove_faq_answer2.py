# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-18 21:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0013_faq_answer3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='answer2',
        ),
    ]