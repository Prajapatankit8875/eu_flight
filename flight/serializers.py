from rest_framework import serializers
from .models import Airport, Flight

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'

class FlightSerializer(serializers.ModelSerializer):
    delay_duration = serializers.ReadOnlyField()

    class Meta:
        model = Flight
        fields = '__all__'