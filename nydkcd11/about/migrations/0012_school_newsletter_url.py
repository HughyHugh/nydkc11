# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-04 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0011_remove_faq_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='newsletter_url',
            field=models.URLField(default=b'#', max_length=300),
        ),
    ]