from django.db import models

# Create your models here.


class Geolocation (models.Model):
    name = models.CharField(max_length=30)
    Latitude = models.DecimalField(max_digits=9, decimal_places=6)
    Longitude = models.DecimalField(max_digits=9, decimal_places=6)


    def __str__(self):
        return self.name