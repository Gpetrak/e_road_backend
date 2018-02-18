from django.contrib.gis import admin
from e_road.models import Event


admin.site.register(Event, admin.OSMGeoAdmin)
