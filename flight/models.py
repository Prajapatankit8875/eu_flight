from django.db import models

# Create your models here.
class Airport(models.Model):
    airport_name = models.CharField(max_length=50)
    iata_code = models.CharField(max_length=10)
    icao_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()

    
class Airline(models.Model):
    airline_name = models.CharField(max_length=50)
    iata_code = models.CharField(max_length=10)
    icao_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)   

    

class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departure_airport')
    arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrival_airport')
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price_per_ticket = models.FloatField()   

    def delay(self):
        if self.departure_time > self.arrival_time:
            return (self.departure_time - self.arrival_time).seconds
        else:
            return 0