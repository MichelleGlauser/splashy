# coding=utf-8
from __future__ import unicode_literals

from django.conf.urls import patterns, include, url
from splashy_app import views
from django.conf import settings

if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^$', views.index, name='index')
    )