# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-07 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_articles', '0002_auto_20171207_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepluginmodel',
            name='alignment',
            field=models.CharField(blank=True, choices=[('left', 'left'), ('right', 'right'), ('center', 'center')], max_length=10, null=True, verbose_name='image alignment'),
        ),
        migrations.AddField(
            model_name='sectionpluginmodel',
            name='alignment',
            field=models.CharField(blank=True, choices=[('left', 'left'), ('right', 'right'), ('center', 'center')], max_length=10, null=True, verbose_name='image alignment'),
        ),
    ]
