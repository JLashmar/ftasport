from django.conf.urls import url, include
from . import views as monthly_view
from django.views.generic import TemplateView

app_name = 'cricket'

urlpatterns = [
    #url(r'^home/$', monthly_view.CricketCalendar.as_view(), name='cricket-monthly'),
]
