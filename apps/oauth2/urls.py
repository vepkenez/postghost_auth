#-*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
        (r'^missing_redirect_uri/?$',   'apps.oauth2.views.missing_redirect_uri'),
        (r'^authorize/?$',              'apps.oauth2.views.authorize'),
        (r'^token/?$',                  'oauth2app.token.handler'),
)