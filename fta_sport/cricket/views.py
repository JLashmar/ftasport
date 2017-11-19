from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
# Create your views here.


from cricket.models import Tour, Match, InningsScorecard, BattingDetail, BowlingDetail, CricketPlayer, FallofWicket


class CricketDetail(generic.DetailView): #maybe change to a list view?
    model = Match
    template_name="cricket/cricket_scorecard.html"
    context_object_name='cricket_score_card'

    def get_context_data(self, **kwargs):
        context = super(CricketDetail, self).get_context_data(**kwargs)
        context['tour'] = Tour.objects.all()
        context['inningsscorecard'] = InningsScorecard.objects.filter(id=self.object.pk)
        context['battingdetail'] = BattingDetail.objects.filter(id=self.object.pk)
        context['bowlingdetail'] = BowlingDetail.objects.filter(id=self.object.pk)
        context['cricketplayer'] = CricketPlayer.objects.filter(id=self.object.pk)
        context['fallofwicket'] = FallofWicket.objects.filter(id=self.object.pk)
        return context

    def get_object(self):

        obj = get_object_or_404(
            self.model,
            pk=self.kwargs['pk'])

        return obj
