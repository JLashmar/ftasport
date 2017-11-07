from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
#my stuff
from sports.models import Sport_Category, Sport
import datetime

class IndexView(generic.ListView):
	template_name="sports/index.html"
	context_object_name='all_sport_category'

	def get_queryset(self):
		return Sport_Category.objects.all()

#unused in templates
class ListView(generic.ListView):
	template_name="sports/sport-category.html"
	context_object_name='category_list'

	def get_queryset(self):
		return Sport_Category.objects.all()

class SportListView(generic.ListView):
	template_name="sports/sport-home.html"
	context_object_name='sport_list'

	def get_queryset(self):
		return Sport.objects.all()
