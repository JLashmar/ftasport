from django.conf.urls import url, include
from . import views as sports_views
from monthly_view import views as monthly_view
from django.views.generic import TemplateView

app_name = 'sports'

urlpatterns = [
    url(r'^(?P<sport_slug>[-_\w]+)/$', sports_views.SportListView.as_view(), name='sport-home'),
    #url(r'^monthly-view/$', monthly_view.IndexView.as_view(), name='monthly-index'),
    url(r'^(?P<category_slug>[-_\w]+)/$', sports_views.ListView.as_view(), name='sport-category'),
    url(r'^$', sports_views.IndexView.as_view(), name='index'),
]
