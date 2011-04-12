from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'events.views.home', name='home'),
    # url(r'^events/', include('events.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^events/list/$', 'events.views.event_list', name='event_list'),
     url(r'^event/form/new/$', 'events.views.event_add', name='event_add'),
     url(r'^event/form/(?P<id>\d+)/$', 'events.views.event_form', name='event_edit'),
     url(r'^event/(?P<slug>[-\w]+)/$', 'events.views.event_detail', name='event_detail'),
)
