from django.urls import path
from .views import BookFlightView, CheckRefundView

urlpatterns = [
    path('bookings/book/', BookFlightView.as_view(), name='book-flight'),
    path('bookings/check_refund/<int:booking_id>/', CheckRefundView.as_view(), name='check-refund'),
]

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import BookingViewSet

# router = DefaultRouter()
# router.register(r'bookings', BookingViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     path('book_flight/', BookingViewSet.as_view({'post': 'book_flight'}), name='book_flight'),
# ]
