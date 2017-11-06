from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
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
    template_name = 'articles/post-detail.html'
    slug_field = 'slug'

    def get_slug_field(self):
        return self.slug_field

    def post_projects(self):
        self.post = get_object_or_404(Post, slug=self.kwargs['slug'])
        return Post.objects.filter(Post=self.post)
