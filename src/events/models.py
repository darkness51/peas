from hashlib import md5
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models import permalink


class EventType(models.Model):
    name = models.CharField(max_length=150)
    
    def __unicode__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(editable=False,unique=True)
    description = models.TextField()
    type = models.ForeignKey(EventType, blank=True, null=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    address = models.TextField()
    location = models.CharField(max_length=150)
    is_public = models.BooleanField(default=False)
    image = models.ImageField(upload_to='event/%y/%m/%d/',
                              blank=True, null=True)
    user = models.ForeignKey(User)
    
    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.name
    
    def save(self):
        self.slug = slugify(self.name)
        super(Event, self).save()
    
    @permalink
    def get_absolute_url(self):
        return ('event_detail', (), {'slug':self.slug})
    
class Photo(models.Model):
    event = models.ForeignKey(Event)
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
    user = models.ForeignKey(User)
    description = models.TextField()
    added = models.DateTimeField(editable = False, auto_now_add=True)
    

RSVP_STATUS_CHOICES = (
    ('N', 'not attending'),
    ('A', 'attending'),
    ('M', 'maybe attending'),               
)

class Invitation(models.Model):    
    event = models.ForeignKey(Event)
    email = models.EmailField()
    sent = models.BooleanField()
    status = models.CharField(max_length=1, blank=True, null=True,
                              choices=RSVP_STATUS_CHOICES, db_index=True)
    hash = models.CharField(max_length=32, editable=False, db_index=True)
    
    def save(self, **kwargs):
        self.hash = md5('%s%s' % (self.id, settings.SECRET_KEY)).hexdigest()
        super(Invitation, self).save(**kwargs)
