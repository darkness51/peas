from django.contrib import admin
from pevents.models import Event, EventType, Photo, Invitation

admin.site.register(Event)
admin.site.register(EventType)
admin.site.register(Photo)
admin.site.register(Invitation)
