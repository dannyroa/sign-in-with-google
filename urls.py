from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns =  patterns('',(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
	{'document_root': settings.STATIC_DOC_ROOT}))

urlpatterns += patterns('',
    # Examples:
    url(r'^$', direct_to_template, {'template': 'index.html'}),
    url(r'^google/', include('sign_in_with_google.google.urls')),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name="auth_logout"),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
