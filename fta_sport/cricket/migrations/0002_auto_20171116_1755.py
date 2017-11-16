# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='battingdetail',
            name='balls_faced',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='battingdetail',
            name='fours',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='battingdetail',
            name='sixes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='battingdetail',
            name='strike_rate',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='inningsscorecard',
            name='byes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='inningsscorecard',
            name='leg_byes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='inningsscorecard',
            name='no_ball',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='inningsscorecard',
            name='penelty_runs',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='inningsscorecard',
            name='wides',
            field=models.IntegerField(default=0),
        ),
    ]