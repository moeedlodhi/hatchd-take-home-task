from django.urls import path, include
from parking_lot import views


urlpatterns = [

    path('parkinglot/',views.ParkingLotView.as_view())
    
]