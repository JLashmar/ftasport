from django.shortcuts import render
from django.views import generic

# Create your views here.

class GolfDetail(generic.DetailView):
    hi = 'golf thing'

    print(hi)
