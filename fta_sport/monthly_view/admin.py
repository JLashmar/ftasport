from django.contrib import admin
from sports.models import Sport_Category, Sport, Gender, Tier, MatchType #used to have Team too
from cricket.models import InningsScorecard, Match
from .models import CricketMonthlyView
# Register your models here.



@admin.register(CricketMonthlyView)
class CricketMonthlyViewAdmin(admin.ModelAdmin):
    list_display = ('date','match_format')

#'home_team', 'away_team'
