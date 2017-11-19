# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 14:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0001_initial'),
        ('rugby', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='bonus_points',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='competition',
            name='drawn',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='competition',
            name='games_played',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='competition',
            name='lost',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='competition',
            name='points_against',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='competition',
            name='points_for',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='competition',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sports.Team'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='competition',
            name='total_points',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='competition',
            name='won',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
