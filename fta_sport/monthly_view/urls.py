from django.conf.urls import url, include
from . import views as monthly_view
from django.views.generic import TemplateView

app_name = 'monthly_view'

urlpatterns = [
    url(r'^monthly-view/$', monthly_view.CricketCalendar.as_view(), name='cricket-monthly'),
]
