from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Airport, Flight
from .serializers import AirportSerializer, FlightSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    @action(detail=False, methods=['get'])
    def delayed_flights(self, request):
        flights = Flight.objects.filter(status="Delayed")
        serializer = self.get_serializer(flights, many=True)
        return Response(serializer.data)