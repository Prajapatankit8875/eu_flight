from django.db import models
from flight.models import Flight
from passengers.models import Passenger

class Booking(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, related_name='bookings')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='bookings')
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)
    refunded = models.BooleanField(default=False)

    def check_refund_eligibility(self):
        if self.flight.delay_duration() > 2 and not self.refunded:
            return True
        return False

    def refund_amount(self):
        return self.ticket_price if self.check_refund_eligibility() else 0

    def __str__(self):
        return f"{self.passenger.name} - {self.flight.flight_number}"