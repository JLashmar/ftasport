from django.conf.urls import url, include
from . import views as cricket
from django.views.generic import TemplateView

app_name = 'cricket'

urlpatterns = [
    url(r'^scorecard/(?P<pk>\d+)/$', cricket.CricketDetail.as_view(), name='cricket-scorecard'),
]
