# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import FlightViewSet

# router = DefaultRouter()
# router.register(r'flights', FlightViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

from django.urls import path
from .views import FlightListView, DelayedFlightListView

urlpatterns = [
    path('flights/', FlightListView.as_view(), name='flight-list'),
    path('flights/delayed/', DelayedFlightListView.as_view(), name='delayed-flights'),
]
