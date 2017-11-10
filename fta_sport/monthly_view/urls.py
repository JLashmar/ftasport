from django.conf.urls import url, include
from . import views as monthly_view
from django.views.generic import TemplateView

app_name = 'monthly_view'

urlpatterns = [
    url(r'^$', monthly_view.IndexView.as_view(), name='monthly-index'),
]
