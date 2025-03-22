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


# from django.db import models

# # Airport Model
# class Airport(models.Model):
#     name = models.CharField(max_length=255)
#     iata_code = models.CharField(max_length=3, unique=True)
#     icao_code = models.CharField(max_length=4, unique=True)
#     country = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     latitude = models.FloatField()
#     longitude = models.FloatField()

#     def __str__(self):
#         return f"{self.name} ({self.iata_code})"

# # Flight Model
# class Flight(models.Model):
#     flight_number = models.CharField(max_length=10, unique=True)
#     airline = models.CharField(max_length=100)
#     departure_airport = models.ForeignKey(Airport, related_name='departures', on_delete=models.CASCADE)
#     arrival_airport = models.ForeignKey(Airport, related_name='arrivals', on_delete=models.CASCADE)
#     scheduled_departure = models.DateTimeField()
#     actual_departure = models.DateTimeField(null=True, blank=True)
#     scheduled_arrival = models.DateTimeField()
#     actual_arrival = models.DateTimeField(null=True, blank=True)
#     status = models.CharField(max_length=20, choices=[('On Time', 'On Time'), ('Delayed', 'Delayed'), ('Cancelled', 'Cancelled')])

#     def delay_duration(self):
#         if self.actual_arrival and self.scheduled_arrival:
#             delay = (self.actual_arrival - self.scheduled_arrival).total_seconds() / 3600
#             return delay if delay > 0 else 0
#         return 0

#     def __str__(self):
#         return f"{self.flight_number} - {self.departure_airport} to {self.arrival_airport}"

# # Passenger Model
# class Passenger(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=15)

#     def __str__(self):
#         return self.name

# # Booking Model
# class Booking(models.Model):
#     passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, related_name='bookings')
#     flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='bookings')
#     ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
#     booking_date = models.DateTimeField(auto_now_add=True)
#     refunded = models.BooleanField(default=False)

#     def check_refund_eligibility(self):
#         if self.flight.delay_duration() > 2 and not self.refunded:
#             return True
#         return False

#     def refund_amount(self):
#         return self.ticket_price if self.check_refund_eligibility() else 0

#     def __str__(self):
#         return f"{self.passenger.name} - {self.flight.flight_number}"
