from django.conf.urls import url, include
from . import views as articles_views
from django.views.generic import TemplateView

app_name = 'articles'

urlpatterns = [
    url(r'^(?P<slug>[-_\w]+)/$', articles_views.DetailView.as_view(), name='article-detail'),
    url(r'^', articles_views.IndexView.as_view(), name='index'),
]
