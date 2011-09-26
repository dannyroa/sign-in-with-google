from django.conf.urls.defaults import *


urlpatterns = patterns('google.views',
   	url(r'^login/$', 'google_login', name="google_login"),
    url(r'^callback/$', 'google_callback', name="google_callback"),
)







    