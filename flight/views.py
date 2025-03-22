from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from models import Airport, Flight, Passenger, Booking
from flights.models import Flight
from passengers.models import Passenger

# Serializer for Booking
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

# API ViewSet for Booking
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    @action(detail=False, methods=['post'])
    def book_flight(self, request):
        """ API to allow a passenger to book a flight on a specific date with a specified amount. """
        passenger_id = request.data.get('passenger_id')
        flight_id = request.data.get('flight_id')
        ticket_price = request.data.get('ticket_price')

        if not passenger_id or not flight_id or not ticket_price:
            return Response({"error": "Missing required fields."}, status=400)

        passenger = get_object_or_404(Passenger, id=passenger_id)
        flight = get_object_or_404(Flight, id=flight_id)

        booking = Booking.objects.create(
            passenger=passenger,
            flight=flight,
            ticket_price=ticket_price
        )

        return Response({"message": "Booking successful", "booking_id": booking.id}, status=201)
