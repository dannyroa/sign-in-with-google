from django.contrib.auth.models import User
from django.conf import settings
from django.core.urlresolvers import reverse

from google.models import GoogleProfile
from google.lib import *

class GoogleAuthBackend:

    @ staticmethod
    def authenticate(access_token):
        #import ipdb; ipdb.set_trace()

        email = get_email(access_token)
        user_info = get_user_info(access_token)
        google_id = user_info['id']
        
        try:
            profile = GoogleProfile.objects.get(google_id=google_id)
            profile.user.backend='google.backends.GoogleAuthBackend' 
            return profile.user
        except GoogleProfile.DoesNotExist:

            display_name = user_info['displayName']

            username = generate_username(display_name)
            
            user = User(username=username, email=email)
            user.first_name, user.last_name = parse_name(display_name)
            user.save()

            image_url = None
            if user_info.has_key('image'):
                image_url = user_info['image'].get('url', None)

            about = user_info['aboutMe']
            location = None

            if user_info.has_key('placesLived'):
                for places in user_info['placesLived']:
                    if places.get('primary', False):
                        location = places['value']
                        break

            profile = GoogleProfile(user=user, google_id=google_id, access_token=access_token)
            profile.image_url = image_url
            profile.location = location
            profile.about = about
            profile.save()

            user.backend='google.backends.GoogleAuthBackend'
            return user       

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None