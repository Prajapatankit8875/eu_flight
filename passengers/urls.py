# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import PassengerViewSet

# router = DefaultRouter()
# router.register(r'passengers', PassengerViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

from django.urls import path
from .views import PassengerListView

urlpatterns = [
    path('passengers/', PassengerListView.as_view(), name='passenger-list'),
]
