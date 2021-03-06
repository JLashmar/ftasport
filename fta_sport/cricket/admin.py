from django.contrib import admin
from .models import Tour, Match, InningsScorecard, CricketPlayer, BattingDetail, BowlingDetail, FallofWicket
from sports.models import Team
# Register your models here.

@admin.register(CricketPlayer)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'international_team')

    #def formfield_for_foreignkey(self, db_field, request, **kwargs):
        #if db_field.name == 'international_team':
            #kwargs['queryset'] = Team.objects.filter(team_name=request.team_name)
        #return super(PlayerAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')

@admin.register(Match)
class CricketScorecardAdmin(admin.ModelAdmin):
    list_display = ('id','tour','start_date', 'end_date','home_team', 'away_team')

@admin.register(InningsScorecard)
class CricketInningsScorecardAdmin(admin.ModelAdmin):
    list_display = ('fixture', 'team')

@admin.register(BattingDetail)
class TourAdmin(admin.ModelAdmin):
    list_display = ('player', 'runs')

@admin.register(BowlingDetail)
class TourAdmin(admin.ModelAdmin):
    list_display = ('player', 'wickets')

@admin.register(FallofWicket)
class TourAdmin(admin.ModelAdmin):
    list_display = ('match','innings', 'wicket', 'runs', 'batsman')
