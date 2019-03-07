from django.conf.urls import patterns, url
from e_road.views import datastore

urlpatterns = patterns(
        'e_road',
        url(r'^results/', datastore, name = 'datastore'),
        )
