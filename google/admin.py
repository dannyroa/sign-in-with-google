from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


from google.models import *

class GoogleProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at']
    search_fields = ['user']


admin.site.register(GoogleProfile, GoogleProfileAdmin)



