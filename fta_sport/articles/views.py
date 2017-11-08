from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import (
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
    )

from articles.models import Post, Sport

# Create your views here.

class IndexView(generic.ListView):
	template_name="articles/index.html"
	context_object_name='all_posts'

	def get_queryset(self):
		return Post.objects.all()

class DetailView(generic.DetailView):
    queryset = Post.objects.all()
    template_name = 'articles/post-details.html'
    slug_field = 'post_slug'

    def get_slug_field(self):
        return self.slug_field

    def post_projects(self):
        self.post = get_object_or_404(Post, slug=self.kwargs['post_slug'])
        return Post.objects.filter(post=self.post)
