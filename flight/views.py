from django.shortcuts import render
from .models import airport, airline, flight, passenger
# Create your views here.
class AirportListView(ListView):
    model = airport
    template_name = 'flight/airport_list.html'
    context_object_name = 'airport_list'  

class FlightListView(ListView):
    model = flight
    template_name = 'flight/flight_list.html'
    context_object_name = 'flight_list'

class AirlineListView(ListView):
    model = airline
    template_name = 'flight/airline_list.html'
    context_object_name = 'airline_list'
    

class PassengerListView(ListView):      
    model = passenger
    template_name = 'flight/passenger_list.html'
    context_object_name = 'passenger_list'
    return render(request, 'flight/passenger_list.html', {'passenger_list': passenger_list})      

