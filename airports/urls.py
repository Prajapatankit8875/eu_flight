# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import AirportViewSet

# router = DefaultRouter()
# router.register(r'airports', AirportViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

from django.urls import path
from .views import AirportListView

urlpatterns = [
    path('airports/', AirportListView.as_view(), name='airport-list'),
]
