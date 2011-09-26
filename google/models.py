import simplejson
import datetime
import facebook
import urllib

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save, post_save, pre_delete
from django.utils.translation import ugettext_lazy as _


class GoogleProfile(models.Model):

    user = models.OneToOneField(User)
    google_id = models.CharField(unique=True, db_index=True, max_length=50)
    access_token = models.CharField(max_length=255)

    image_url = models.URLField(null=True, blank=True)
    about = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.user.username
 

