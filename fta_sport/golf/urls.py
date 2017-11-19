from django.conf.urls import url, include
from . import views as golf
from django.views.generic import TemplateView

app_name = 'golf'

urlpatterns = [
    url(r'^scorecard/(?P<pk>\d+)/$', golf.GolfDetail.as_view(), name='golf-scorecard'),
]
