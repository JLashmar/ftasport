from django.db import models
from datetime import datetime
from sports.models import Team, MatchType
from django_countries.fields import CountryField

# Create your models here.

class CricketPlayer(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    second_name = models.CharField(max_length=50, blank=True)
    international_team = models.ForeignKey('sports.Team', on_delete=models.CASCADE, related_name='international_team')
    domestic_teams = models.ManyToManyField('sports.Team', related_name='domestic_teams')

class Tour(models.Model):
    name = models.CharField(max_length=200)
    country = CountryField()

    def __unicode__(self):
        return str(self.name)

class Match(models.Model):
    tour = models.ForeignKey('Tour', on_delete=models.CASCADE)
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)
    home_team = models.ForeignKey('sports.Team', on_delete=models.CASCADE, related_name='home_team')
    away_team = models.ForeignKey('sports.Team', on_delete=models.CASCADE, related_name='away_team')

class InningsScorecard(models.Model):
    fixture = models.ForeignKey(Match)
    team = models.ForeignKey(Team)
    runs = models.IntegerField(default=0)
    wides = models.IntegerField(default=0)
    no_ball = models.IntegerField(default=0)
    leg_byes = models.IntegerField(default=0)
    byes = models.IntegerField(default=0)
    penelty_runs = models.IntegerField(default=0)
    wickets = models.IntegerField(default=0)
    overs = models.FloatField(default=0.0)

    def __unicode__(self):
        return str(self.team)

class BattingDetail(models.Model):
    STATUS_CHOICES = (
        ('NO', 'not out'),
        ('bowled', 'bowled'),
        ('caught', 'caught'),
        ('lbw', 'lbw'),
        ('stumped', 'stumped'),
        ('ran-out', 'ran-out'),
        ('retired-hurt', 'retired-hurt'),
        ('retired-out', 'retired-out'),
        ('timed-out', 'timed-out'),
        ('handled-the-ball', 'handled-the-ball'),
    )
    innings = models.ForeignKey(InningsScorecard)
    player = models.ForeignKey(CricketPlayer)
    runs = models.IntegerField(default=0)
    balls_faced = models.IntegerField(default=0)
    fours = models.IntegerField(default=0)
    sixes = models.IntegerField(default=0)
    strike_rate = models.IntegerField(default=0)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='NO')

    def __unicode__(self):
        return str(self.player)

class BowlingDetail(models.Model):
    innings = models.ForeignKey(InningsScorecard)
    player = models.ForeignKey(CricketPlayer)
    runs = models.IntegerField(default=0)
    maidens = models.IntegerField(default=0)
    wickets = models.IntegerField(default=0)
    overs = models.FloatField(default=0.0)
    economy = models.FloatField(default=0.0)

    def __unicode__(self):
        return str(self.player)
