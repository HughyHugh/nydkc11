# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-11 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20171128_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='blurb',
            field=models.CharField(max_length=300, verbose_name='Short Summary of Article'),
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(verbose_name='Body of Article'),
        ),
        migrations.AlterField(
            model_name='image',
            name='desc',
            field=models.CharField(max_length=1000, verbose_name='Short Image Description'),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=1000, verbose_name='Image Title'),
        ),
        migrations.AlterField(
            model_name='link',
            name='host',
            field=models.CharField(max_length=50, verbose_name='Hosting School/Organization'),
        ),
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.CharField(max_length=1000, verbose_name='Signup Sheet/Link'),
        ),
        migrations.AlterField(
            model_name='post',
            name='blurb',
            field=models.CharField(max_length=300, verbose_name='Short Summary of Post'),
        ),
    ]
