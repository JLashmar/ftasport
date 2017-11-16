from django.db import models
from datetime import datetime

from sports.models import Sport
from cricket.models import InningsScorecard, Match

# Create your models here.

class MonthlyView(models.Model):
    sport_name = models.ForeignKey('sports.sport', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)

class CricketMonthlyView(models.Model):
    match_id = models.ForeignKey('cricket.Match', on_delete=models.CASCADE)
    match_format = models.ForeignKey('sports.MatchType', on_delete=models.CASCADE, related_name='match_format') #List-A or First Class
    date = models.DateTimeField(blank=True)
    #home team info
    #home_team = models.ForeignKey('cricket.Match', on_delete=models.CASCADE, related_name='home')
    #away team info
    #away_team = models.ForeignKey('cricket.Match', on_delete=models.CASCADE, related_name='away')
