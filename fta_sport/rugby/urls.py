from django.conf.urls import url, include
from . import views as rugby_views
from django.views.generic import TemplateView

app_name = 'rugby'

urlpatterns = [
    url(r'^scorecard/(?P<pk>\d+)/$', rugby_views.RugbyDetail.as_view(), name='rugby-scorecard'),
]
