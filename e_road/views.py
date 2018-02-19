from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.gis.geos import Point
from e_road.models import Event
from django.db.models.loading import get_model
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt 
def datastore(request):
    if request.method == 'POST':
        # convert json data to python dictionary
        desc_loc =json.loads(request.body)
        title = desc_loc['title']
        description = desc_loc['desc']
        latitude = desc_loc['lat']
        longitude = desc_loc['lon']
       
        
      #  latitude = float(latitude)
      #  longitude = float(logitude)

        location = Point(longitude, latitude, srid=4326)

        e1 = Event(title = title,
                   description = description,
                   location = location)

        e1.save()
     
        # check if e1 saved
        if e1.pk is None:
            return HttpResponse("Upload failed")
        else:
            return HttpResponse("Success")
