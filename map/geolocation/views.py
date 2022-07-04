from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .models import Geolocation
from rest_framework import status
from .serializers import GeolocationSerializer
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
 
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
# Create your views here.


#list all location
@api_view(['GET'])
def view_location(request):
    # cheching lication in cache
    if 'location' in cache:
        # get results from cache
        result = cache.get('location')
        return Response(result.data)
    else:
        locations = Geolocation.objects.all()
        if locations:
            result = GeolocationSerializer(locations,many=True) 
            # store data in cache
            cache.set('location',result,timeout=CACHE_TTL)
            return Response(result.data)

        else:
            return Response({"status": "error", "data": "Data not found"}, status=status.HTTP_400_BAD_REQUEST)

#display location based on id
@api_view(['GET'])
def location_detail(request, id):
    # cache.delete(id)
    if cache.get(id):
        location=cache.get(id)
        return Response({"status": "success", "data": location.data}, status=status.HTTP_200_OK)
    else:
        try:
            location = Geolocation.objects.get(id=id)
            print(location)
            
            serializer = GeolocationSerializer(location)
            cache.set(id,serializer)
            return Response({"status": "success","data":serializer.data}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print (e)
            return Response({"status": "error", "data": str(e)}, status=status.HTTP_200_OK)

  
        