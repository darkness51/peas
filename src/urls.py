from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',
     url(r'^admin/', include(admin.site.urls)),
     url(r'^event/', include('events.urls')),
     url(r'^auth/', include('social_auth.urls')),
     url(r'^auth/login/$', direct_to_template, {'template': 'login.html'}, name='login'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^(?P<path>.*\.(?i)(css|js|jpg|jpeg|png|gif|ico|swf|html|htm))$', 
         'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
