from django.core.management.base import BaseCommand
from flight.models import Airport, Flight
from datetime import datetime, timedelta
import random

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        airports = [
            {"name": "Frankfurt Airport", "iata_code": "FRA", "icao_code": "EDDF", "country": "Germany", "city": "Frankfurt", "latitude": 50.0333, "longitude": 8.5706},
            {"name": "Munich Airport", "iata_code": "MUC", "icao_code": "EDDM", "country": "Germany", "city": "Munich", "latitude": 48.3538, "longitude": 11.7861},
            {"name": "Berlin Brandenburg", "iata_code": "BER", "icao_code": "EDDB", "country": "Germany", "city": "Berlin", "latitude": 52.3667, "longitude": 13.5033},
        ]

        for airport in airports:
            Airport.objects.get_or_create(**airport)

        flights = [
            {"flight_number": "LH123", "departure_airport": "FRA", "arrival_airport": "MUC", "scheduled_departure": datetime.now(), "scheduled_arrival": datetime.now() + timedelta(hours=1)},
            {"flight_number": "LH456", "departure_airport": "MUC", "arrival_airport": "BER", "scheduled_departure": datetime.now(), "scheduled_arrival": datetime.now() + timedelta(hours=2)},
        ]

        for flight in flights:
            Flight.objects.get_or_create(
                flight_number=flight["flight_number"],
                departure_airport=Airport.objects.get(iata_code=flight["departure_airport"]),
                arrival_airport=Airport.objects.get(iata_code=flight["arrival_airport"]),
                scheduled_departure=flight["scheduled_departure"],
                scheduled_arrival=flight["scheduled_arrival"],
                actual_departure=flight["scheduled_departure"] + timedelta(minutes=random.randint(0, 180)),  # Simulating delays
                actual_arrival=flight["scheduled_arrival"] + timedelta(minutes=random.randint(0, 180)),
                status="Delayed" if random.choice([True, False]) else "On Time"
            )

        self.stdout.write(self.style.SUCCESS("Successfully populated the database"))