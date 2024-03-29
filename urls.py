from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    (r'^', include('apps.base.urls')),
    (r'^account/', include('apps.account.urls')),
    (r'^client/', include('apps.client.urls')),
    (r'^oauth2/', include('apps.oauth2.urls')),
    (r'^api/', include('apps.api.urls')),
)
