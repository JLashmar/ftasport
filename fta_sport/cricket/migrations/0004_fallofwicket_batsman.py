# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 11:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cricket', '0003_auto_20171118_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='fallofwicket',
            name='batsman',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='batsman_dismissed', to='cricket.BattingDetail'),
        ),
    ]
