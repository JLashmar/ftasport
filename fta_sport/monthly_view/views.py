from django.shortcuts import render
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
# Create your views here.

from .models import MonthlyView, CricketMonthlyView, RugbyMonthlyView

from cricket.models import Tour, Match

from rugby.models import Competition, Match

class CricketCalendar(generic.ListView):
	template_name="monthly_view/cricket-monthly-view.html"
	context_object_name='cricket_monthly_view'
	queryset = CricketMonthlyView.objects.all()

	def get_context_data(self, **kwargs):
		context = super(CricketCalendar, self).get_context_data(**kwargs)
		context['tour'] = Tour.objects.all()
		context['match'] = Match.objects.all()
		return context

class RugbyMonthlyView(generic.ListView):
	template_name="monthly_view/rugby-monthly-view.html"
	context_object_name='rugby_monthly_view'
	queryset = RugbyMonthlyView.objects.all()

	def get_context_data(self, **kwargs):
		context = super(RugbyMonthlyView, self).get_context_data(**kwargs)
		context['competition'] = Competition.objects.all()
		context['match'] = Match.objects.all()
		return context
