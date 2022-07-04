import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import Geolocation
from .serializers import GeolocationSerializer


# initialize the APIClient app
client = Client()


class GetAllExperimentTest(TestCase):

    """ Test module for GET all experiments API """

    def setUp(self):
        # print("herrrrrrr")
        Geolocation.objects.create(
            name='location1', Latitude=0.00002, Longitude=0.00003)
        Geolocation.objects.create(
            name='location2', Latitude=0.00002, Longitude=0.00003)
        Geolocation.objects.create(
            name='location3',Latitude=0.00002, Longitude=0.00003)
    
    def test_get_all_location(self):
        # url = reverse('api-jwt-auth')
        url='/account/api/token/'
        print(url)
        resp = self.client.post(url, {"email":"silpa.tp@gmail.com", "password":"1234"})
        print(resp)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in resp.data)
        token = resp.data['token']
        client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        response = client.get(reverse('location_list'))
        print(response)
        # location = Geolocation.objects.all()
        # serializer = GeolocationSerializer(location, many=True)
        # self.assertEqual(response.data, serializer.data)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)