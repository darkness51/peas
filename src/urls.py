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
     url(r'^event/form/invitation/(?P<slug>[-\w]+)/$', 'events.views.send_invitation', name='send_invitation'),
     url(r'^event/form/response/(?P<id>\d+)/$', 'events.views.response_invitation', name='response_invitation'),
     url(r'^event/form/(?P<id>\d+)/$', 'events.views.event_form', name='event_edit'),
     url(r'^event/(?P<slug>[-\w]+)/$', 'events.views.event_detail', name='event_detail'),
     url(r'^', include('social_auth.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^(?P<path>.*\.(?i)(css|js|jpg|jpeg|png|gif|ico|swf|html|htm))$', 
         'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )