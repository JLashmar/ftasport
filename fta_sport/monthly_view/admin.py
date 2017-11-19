from django.contrib import admin
from sports.models import Sport_Category, Sport, Gender, Tier, MatchType #used to have Team too
from cricket.models import InningsScorecard, Match
from .models import CricketMonthlyView, RugbyMonthlyView
# Register your models here.


@admin.register(CricketMonthlyView)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'match_id')

admin.site.register(RugbyMonthlyView)

#'home_team', 'away_team'
