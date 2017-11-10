from django.shortcuts import render
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
# Create your views here.

from .models import MonthlyView

class IndexView(generic.ListView):
	template_name="monthly_view/monthly-view.html"
	context_object_name='sport_monthly_view'

	def get_queryset(self):
		return MonthlyView.objects.all()
