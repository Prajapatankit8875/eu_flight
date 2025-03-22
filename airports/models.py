from django.db import models

class Airport(models.Model):
    name = models.CharField(max_length=255)
    iata_code = models.CharField(max_length=3, unique=True)
    icao_code = models.CharField(max_length=4, unique=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.iata_code})"
    