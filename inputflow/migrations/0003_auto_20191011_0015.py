# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-10-11 03:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inputflow', '0002_webhook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webhook',
            name='settings',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='webhooks', to='inputflow.InputSettings', verbose_name='Settings'),
        ),
    ]