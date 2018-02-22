from django.contrib.gis.db import models
from django.forms import ModelForm
from django.forms import Textarea
from datetime import datetime

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    location = models.PointField()
    image = models.ImageField('img', upload_to='images/')
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title or u''

# Build the Textarea
class EventModelForm(ModelForm):
    class Meta:
        model = Event
        widgets = {
                'abstract': Textarea(attrs={'cols': 80, 'rows': 20}),
                }
