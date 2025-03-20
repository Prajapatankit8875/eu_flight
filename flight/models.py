from django.db import models

# Create your models here.
class airport(models.Model):
    airport_name = models.CharField(max_length=100)
    iata_code = models.CharField(max_length=10)
    icao_code = models.CharField(max_length=10)
    country = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    latitude = models.FloatField()
    longitude = models.FloatField()

    
    def __str__(self):
        return self.airport_name 
    
    

