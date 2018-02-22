from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.gis.geos import Point
from e_road.models import Event
from django.db.models.loading import get_model
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.files.storage import FileSystemStorage
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
        
        location = Point(longitude, latitude, srid=4326)
        
        if request.FILES.get('image'):
            # image store
            myimage = request.FILES.get('image')
            fs = FileSystemStorage()
            filename = fs.save(myimage.name, myimage)
            uploaded_file_url = fs.url(filename)
        
            e1 = Event(title = title,
                   description = description,
                   location = location,
                   image = image)

        else:
            e1 = Event(title = title,
            description = description,
            location = location
                      )


        e1.save()
     
        # check if e1 saved
        if e1.pk is None:
            return HttpResponse("Upload failed")
        else:
            return HttpResponse("Success")

