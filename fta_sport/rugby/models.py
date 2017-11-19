from django.db import models
from datetime import datetime
from sports.models import Team, MatchType, Tier
from django_countries.fields import CountryField

# Create your models here.

class RugbyPlayer(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    second_name = models.CharField(max_length=50, blank=True)
    international_team = models.ForeignKey('sports.Team', on_delete=models.CASCADE, related_name='rugby_international_team')
    domestic_teams = models.ManyToManyField('sports.Team', related_name='rugby_domestic_teams')

class Competition(models.Model):
    name = models.CharField(max_length=200)
    tier_level = models.ForeignKey('sports.Tier')
    country = CountryField()

    def __unicode__(self):
        return str(self.name)

class Match(models.Model):
    competition = models.ForeignKey('Competition', on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True)
    home_team = models.ForeignKey('sports.Team', on_delete=models.CASCADE, related_name='rugby_home_team')
    away_team = models.ForeignKey('sports.Team', on_delete=models.CASCADE, related_name='rugby_away_team')

class MatchScorecard(models.Model): #maybe rename teamscorecard?
    fixture = models.ForeignKey(Match)
    team = models.ForeignKey(Team)
    score =  models.IntegerField(default=0)

    #def __unicode__(self):
        #return str(self.team)

class PlayerDetail(models.Model):
    fixture = models.ForeignKey(MatchScorecard)
    player = models.ForeignKey(RugbyPlayer)
    team = models.ForeignKey(Team)

    #def __unicode__(self):
        #return str(self.player)
