from django.contrib import admin
from .models import RugbyPlayer, Competition, CompetitionDetail, Match, MatchScorecard, PlayerDetail
from sports.models import Team
# Register your models here.

@admin.register(RugbyPlayer)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'international_team')

    #def formfield_for_foreignkey(self, db_field, request, **kwargs):
        #if db_field.name == 'international_team':
            #kwargs['queryset'] = Team.objects.filter(team_name=request.team_name)
        #return super(PlayerAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(Competition)
class TourAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')

@admin.register(CompetitionDetail)
class TourAdmin(admin.ModelAdmin):
    list_display = ('competition', 'team')

@admin.register(Match)
class RugbyScorecardAdmin(admin.ModelAdmin):
    list_display = ('date','home_team', 'away_team')

@admin.register(MatchScorecard)
class RugbyMatchScorecardAdmin(admin.ModelAdmin):
    list_display = ('fixture', 'team')

@admin.register(PlayerDetail)
class RugbyPlayerScorecardAdmin(admin.ModelAdmin):
    list_display = ('player', 'team')
