from django.shortcuts import render
from django.views import generic

# Create your views here.

from .models import Competition, CompetitionDetail, Match, RugbyPlayer, MatchScorecard, PlayerDetail

class RugbyDetail(generic.DetailView): #maybe change to a list view?
    model = Match
    template_name="rugby/rugby-scorecard.html"
    context_object_name='rugby_score_card'

    def get_context_data(self, **kwargs):
        context = super(RugbyDetail, self).get_context_data(**kwargs)
        context['competition'] = Competition.objects.all()
        context['competitiondetail'] = CompetitionDetail.objects.filter(id=self.object.pk)
        context['rugbyplayer'] = RugbyPlayer.objects.filter(id=self.object.pk)
        context['matchscorecard'] = MatchScorecard.objects.filter(id=self.object.pk)
        context['playerdetail'] = PlayerDetail.objects.filter(id=self.object.pk)
        return context
