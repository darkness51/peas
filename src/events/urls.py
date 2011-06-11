from django.conf.urls.defaults import patterns, url
from events.views import EventListView, EventDetailView, EventCreateView

urlpatterns = patterns('events.views',
     url(r'^$', EventListView.as_view(), name='event_list'),
     url(r'^add/$', EventCreateView.as_view(), name='event_add'),
     url(r'^(?P<slug>[-\w]+)/$', EventDetailView.as_view(), name='event_detail'),

     url(r'^form/invitation/(?P<slug>[-\w]+)/$', 'send_invitation', name='send_invitation'),
     #url(r'^form/response/(?P<id>\d+)/(?P<email>[-\w]+)/$', 'response_invitation', name='response_invitation'),
     url(r'^form/(?P<id>\d+)/$', 'event_form', name='event_edit'),
)
