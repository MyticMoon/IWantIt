__author__ = 'Hiep'
from django.conf.urls import patterns, url

from iwantit import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)