import random
from django.core.management.base import BaseCommand
from faker import Faker
from datetime import datetime, timedelta
from airports.models import Airport
from flight.models import Flight
from passengers.models import Passenger
from bookings.models import Booking

fake = Faker()

class Command(BaseCommand):
    help = "Populate database with dummy data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Creating Airports...")
        airports = []
        for _ in range(10):
            airport = Airport.objects.create(
                name=fake.city() + " Airport",
                iata_code=fake.unique.lexify(text="???").upper(),
                icao_code=fake.unique.lexify(text="????").upper(),
                country=fake.country(),
                city=fake.city(),
                latitude=fake.latitude(),
                longitude=fake.longitude(),
            )
            airports.append(airport)

        self.stdout.write("Creating Flights...")
        flights = []
        for _ in range(10):
            departure, arrival = random.sample(airports, 2)
            scheduled_departure = fake.date_time_this_month()
            delay = random.choice([0, 1, 2, 3])  # Random delay in hours
            flight = Flight.objects.create(
                flight_number=fake.unique.bothify(text="FL###"),
                airline=fake.company(),
                departure_airport=departure,
                arrival_airport=arrival,
                scheduled_departure=scheduled_departure,
                actual_departure=scheduled_departure + timedelta(hours=delay),
                scheduled_arrival=scheduled_departure + timedelta(hours=3),
                actual_arrival=scheduled_departure + timedelta(hours=3 + delay),
                status=random.choice(["On Time", "Delayed", "Cancelled"]),
            )
            flights.append(flight)

        self.stdout.write("Creating Passengers...")
        passengers = []
        for _ in range(10):
            passenger = Passenger.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone=fake.phone_number(),
            )
            passengers.append(passenger)

        self.stdout.write("Creating Bookings...")
        for _ in range(10):
            passenger = random.choice(passengers)
            flight = random.choice(flights)
            Booking.objects.create(
                passenger=passenger,
                flight=flight,
                ticket_price=round(random.uniform(100, 1000), 2),
                refunded=random.choice([True, False]),
            )

        self.stdout.write(self.style.SUCCESS("Dummy data created successfully!"))
