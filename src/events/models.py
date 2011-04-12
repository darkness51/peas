from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

class EventType(models.Model):
    name = models.CharField(max_length=150)
    
    def __unicode__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(editable=False,unique=True)
    description = models.TextField()
    type = models.ForeignKey(EventType, blank = True, null =True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    address = models.TextField()
    location = models.CharField(max_length=150)
    is_public = models.BooleanField(default = False)
    user = models.ForeignKey(User)
    
    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.name
    
    def save(self):
        self.slug = slugify(self.name)
        super(Event, self).save()
   
    
class Photo(models.Model):
    event = models.ForeignKey(Event)
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
    user = models.ForeignKey(User)
    description = models.TextField()
    added = models.DateTimeField(editable = False, auto_now_add=True)
    
    
class Invitation(models.Model):
    STATUS_CHOICES = (
        ('R','awaiting reply'),
        ('N', 'not attending'),
        ('A', 'attending')                
    )
    
    event = models.ForeignKey(Event)
    email = models.EmailField()
    sent = models.BooleanField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)    
    