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
    
class flight(models.Model): 
    flight_number = models.CharField(max_length=10)
    departure_airport = models.ForeignKey(airport, on_delete=models.CASCADE)
    arrival_airport = models.ForeignKey(airport, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField() 
    price = models.FloatField()
    duration = models.FloatField()
    status = models.CharField(max_length=15, default='Scheduled', choices=[('Scheduled', 'Scheduled'), ('Delayed', 'Delayed'), ('Cancelled', 'Cancelled')])
    delay_time = models.FloatField()
    
    def __str__(self):
        return self.flight_number
    
class airline(models.Model):
    airline_name = models.CharField(max_length=100)
    iata_code = models.CharField(max_length=10)
    icao_code = models.CharField(max_length=10)
    city = models.CharField(max_length=15)
    logo = models.ImageField(upload_to='airline_logo')
    
    def __str__(self):
        return self.airline_name
    
class passenger(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    passport_number = models.CharField
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)          
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=15)
    country = models.CharField(max_length=15)
    postal_code = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name + self.last_name
    
    
    

