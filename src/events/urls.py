from django.conf.urls.defaults import patterns, url
from events.views import EventListView, EventDetailView, EventCreateView, EventUpdateView, \
                         InvitationView, InvitationRsvpView

urlpatterns = patterns('events.views',
     url(r'^add/$', EventCreateView.as_view(), name='event_add'),
     url(r'^edit/(?P<pk>\d+)/$', EventUpdateView.as_view(), name='event_edit'),

     url(r'^$', EventListView.as_view(), name='event_list'),
     url(r'^(?P<slug>[-\w]+)/$', EventDetailView.as_view(), name='event_detail'),

     url(r'^(?P<slug>[-\w]+)/invite/$', InvitationView.as_view(), name='send_invitation'),
     url(r'^rsvp/(?P<hash>\w+)/$', InvitationRsvpView.as_view(), name='event_rsvp'),
)
