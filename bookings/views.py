


import json
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from bookings.models import Booking
from flight.models import Flight
from passengers.models import Passenger

@method_decorator(csrf_exempt, name='dispatch')
class BookFlightView(View):
    def post(self, request):
        data = json.loads(request.body)
        passenger_id = data.get('passenger_id')
        flight_id = data.get('flight_id')
        ticket_price = data.get('ticket_price')

        if not passenger_id or not flight_id or not ticket_price:
            return JsonResponse({"error": "Missing required fields."}, status=400)

        passenger = get_object_or_404(Passenger, id=passenger_id)
        flight = get_object_or_404(Flight, id=flight_id)

        booking = Booking.objects.create(
            passenger=passenger,
            flight=flight,
            ticket_price=ticket_price
        )

        return JsonResponse({"message": "Booking successful", "booking_id": booking.id})

class CheckRefundView(View):
    def get(self, request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id)
        if booking.check_refund_eligibility():
            return JsonResponse({"message": "Eligible for refund", "refund_amount": float(booking.refund_amount())})
        return JsonResponse({"message": "Not eligible for refund"})
