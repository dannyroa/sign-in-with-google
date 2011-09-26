
from django.utils import simplejson
import urllib
import urllib2

from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext

from google.models import GoogleProfile
from google.backends import *


LOGIN_REDIRECT_URL = getattr(settings, 'LOGIN_REDIRECT_URL', '/')

authenticate_url = 'https://accounts.google.com/o/oauth2/auth'
access_token_url = 'https://accounts.google.com/o/oauth2/token'


def google_login(request):

	next = request.GET.get('next', None)
	if next:
		request.session['google_login_next'] = next
	
	scope = urllib.quote('https://www.googleapis.com/auth/userinfo#email https://www.googleapis.com/auth/plus.me')
	url = '%s?client_id=%s&response_type=code&scope=%s&redirect_uri=%s%s' % (authenticate_url, settings.GOOGLE_CLIENT_ID, scope, settings.DOMAIN, reverse('google_callback'))

	return HttpResponseRedirect(url)

    
def google_callback(request):

    code = request.GET.get('code','')

    redirect_uri = urllib2.quote('%s%s' % (settings.DOMAIN, reverse('google_callback')))
    data = 'client_id=%s&client_secret=%s&grant_type=authorization_code&code=%s&redirect_uri=%s' % (settings.GOOGLE_CLIENT_ID, settings.GOOGLE_CLIENT_SECRET, code, redirect_uri)

    req = urllib2.Request(access_token_url, data=data)
    response = urllib2.urlopen(req)
    response_content = response.read()

    json_response = simplejson.loads(response_content)

    access_token = json_response['access_token']

    #import ipdb; ipdb.set_trace()

    user = GoogleAuthBackend.authenticate(access_token)

    if not user:
    	next = reverse('auth_login')
    else:    
        next = request.session.get('google_login_next', None)
    	if next:
        	del request.session['google_login_next']
        else:
        	next = LOGIN_REDIRECT_URL
        
        login(request, user)
        
    return HttpResponseRedirect(next)
 
