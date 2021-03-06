# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 22:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_image_show_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='other_link',
            field=models.ManyToManyField(blank=True, related_name='links', to='blog.Post', verbose_name=b'Other Related Posts'),
        ),
        migrations.AlterField(
            model_name='link',
            name='link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post', verbose_name=b'Primary Post'),
        ),
    ]
