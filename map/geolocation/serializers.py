from django.db.models import fields
from rest_framework import serializers
from .models import Geolocation
  
class GeolocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geolocation
        fields = ('__all__')