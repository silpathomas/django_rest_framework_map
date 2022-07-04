from django.contrib import admin
from geolocation.models import Geolocation

# Register your models here.
admin.site.register(Geolocation)
list_display = ('name' )