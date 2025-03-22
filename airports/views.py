from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from airports.models import Airport

class AirportListView(View):
    def get(self, request):
        airports = list(Airport.objects.values())
        return JsonResponse({"airports": airports})

