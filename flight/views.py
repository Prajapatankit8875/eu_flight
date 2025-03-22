from django.http import JsonResponse
from django.views import View
from flight.models import Flight

class FlightListView(View):
    def get(self, request):
        flights = list(Flight.objects.values())
        return JsonResponse({"flights": flights})

class DelayedFlightListView(View):
    def get(self, request):
        delayed_flights = list(Flight.objects.filter(status='Delayed').values())
        return JsonResponse({"delayed_flights": delayed_flights})

