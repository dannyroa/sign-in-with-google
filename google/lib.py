import datetime
import urllib2

from django.conf import settings
from django.contrib.auth.models import User
from django.utils import simplejson


    
def get_email(access_token):

    user_info_url = 'https://www.googleapis.com/userinfo/email?alt=json'
    req = urllib2.Request(user_info_url)
    req.add_header("Authorization", "OAuth %s" % access_token)
    response = urllib2.urlopen(req)
    response_content = response.read()
    json_response = simplejson.loads(response_content)
    email = json_response['data']['email']
    return email


def get_user_info(access_token):

    plus_user_info_url = 'https://www.googleapis.com/plus/v1/people/me?pp=1&key=%s' % settings.GOOGLE_API_KEY
    req = urllib2.Request(plus_user_info_url)
    req.add_header("Authorization", "OAuth %s" % access_token)
    response = urllib2.urlopen(req)
    response_content = response.read()
    json_response = simplejson.loads(response_content)

    return json_response


def generate_username(username):

    username = username.replace(' ','').replace('.','').lower()
    if len(username) > 16:
        username = username[0:16]
        
    if User.objects.filter(username=username).exists():
        if len(username) > 14:
            username = username[0:14]
        username = username + str(datetime.datetime.now().second)
    
    return username


def parse_name(name):

    name_array = name.split(' ')
    if len(name.split(' ')) > 1:
        last_name = name_array[len(name_array)-1]
        del name_array[len(name_array)-1:len(name_array)]
        first_name = ' '.join(name_array)
    else:
        first_name = name
        last_name = ''
    
    return first_name, last_name 