from django.contrib.gis.db import models
from django.contrib.auth.models import User
from commonutils.slug import slugify
from tagging.fields import TagField


class EventType(models.Model):
    name = models.CharField(max_length=50)


class Event(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(editable=False)
    type = models.ForeignKey(EventType)
    time = models.DateTimeField(db_index=True)
    address = models.TextField(blank=True, null=True)
    location = models.PointField()
    tags = TagField()
    user = models.ForeignKey(User)

    def save(self, **kwargs):
        self.slug = slugify(self.name)
        super(Event, self).save(**kwargs)


class Photo(models.Model):
    event = models.ForeignKey(Event)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d')
    tags = TagField()
    time = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User)


class Invitation():
    event = models.ForeignKey(Event)
    email = models.EmailField()
    status = models.CharField(max_length=1, db_index=True,
                              blank=True, null=True, 
                              choices=(('w', _('awaiting reply')),
                                       ('a', _('not attending')),
                                       ('n', _('attending'))))
    
    