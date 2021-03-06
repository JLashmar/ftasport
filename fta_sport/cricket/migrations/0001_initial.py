# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 11:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BattingDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('runs', models.IntegerField(default=0)),
                ('balls_faced', models.IntegerField(default=0)),
                ('fours', models.IntegerField(default=0)),
                ('sixes', models.IntegerField(default=0)),
                ('strike_rate', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('NO', 'not out'), ('bowled', 'bowled'), ('caught', 'caught'), ('lbw', 'lbw'), ('stumped', 'stumped'), ('ran-out', 'ran-out'), ('retired-hurt', 'retired-hurt'), ('retired-out', 'retired-out'), ('timed-out', 'timed-out'), ('handled-the-ball', 'handled-the-ball')], default='NO', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='BowlingDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('runs', models.IntegerField(default=0)),
                ('maidens', models.IntegerField(default=0)),
                ('wickets', models.IntegerField(default=0)),
                ('overs', models.FloatField(default=0.0)),
                ('economy', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='CricketPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('second_name', models.CharField(blank=True, max_length=50)),
                ('domestic_teams', models.ManyToManyField(related_name='cricket_domestic_teams', to='sports.Team')),
                ('international_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cricket_international_team', to='sports.Team')),
            ],
        ),
        migrations.CreateModel(
            name='InningsScorecard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('runs', models.IntegerField(default=0)),
                ('wides', models.IntegerField(default=0)),
                ('no_ball', models.IntegerField(default=0)),
                ('leg_byes', models.IntegerField(default=0)),
                ('byes', models.IntegerField(default=0)),
                ('penelty_runs', models.IntegerField(default=0)),
                ('wickets', models.IntegerField(default=0)),
                ('overs', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(blank=True)),
                ('end_date', models.DateTimeField(blank=True)),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cricket_away_team', to='sports.Team')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cricket_home_team', to='sports.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('tier_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sports.Tier')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cricket.Tour'),
        ),
        migrations.AddField(
            model_name='inningsscorecard',
            name='fixture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cricket.Match'),
        ),
        migrations.AddField(
            model_name='inningsscorecard',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sports.Team'),
        ),
        migrations.AddField(
            model_name='bowlingdetail',
            name='innings',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cricket.InningsScorecard'),
        ),
        migrations.AddField(
            model_name='bowlingdetail',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cricket.CricketPlayer'),
        ),
        migrations.AddField(
            model_name='battingdetail',
            name='innings',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cricket.InningsScorecard'),
        ),
        migrations.AddField(
            model_name='battingdetail',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cricket.CricketPlayer'),
        ),
    ]
