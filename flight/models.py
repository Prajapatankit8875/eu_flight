from django.db import models
from airports.models import Airport

class Flight(models.Model):
    flight_number = models.CharField(max_length=10, unique=True)
    airline = models.CharField(max_length=100)
    departure_airport = models.ForeignKey(Airport, related_name='departures', on_delete=models.CASCADE)
    arrival_airport = models.ForeignKey(Airport, related_name='arrivals', on_delete=models.CASCADE)
    scheduled_departure = models.DateTimeField(null=True, blank=True)
    actual_departure = models.DateTimeField(null=True, blank=True)
    scheduled_arrival = models.DateTimeField(null=True, blank=True)
    actual_arrival = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('On Time', 'On Time'), ('Delayed', 'Delayed'), ('Cancelled', 'Cancelled')])

    def delay_duration(self):
        if self.actual_arrival and self.scheduled_arrival:
            delay = (self.actual_arrival - self.scheduled_arrival).total_seconds() / 3600
            return delay if delay > 0 else 0
        return 0

    def __str__(self):
        return f"{self.flight_number} - {self.departure_airport} to {self.arrival_airport}"
    