from django.http import JsonResponse
from django.views import View
from passengers.models import Passenger

class PassengerListView(View):
    def get(self, request):
        passengers = list(Passenger.objects.values())
        return JsonResponse({"passengers": passengers})
