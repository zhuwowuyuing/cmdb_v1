__author__ = 'liangnaihua'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^index.html/$', 'assets.views.index'),
    url(r'^index/$', 'assets.views.index'),
)