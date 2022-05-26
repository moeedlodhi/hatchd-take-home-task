from django.shortcuts import render
from .models import customer,booking
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BookingSerializer
from datetime import datetime,timedelta,date

# Create your views here.


class ParkingLotView(APIView):


    def get(self,request):
        query_date = request.GET.get('query_date')
        query_bookings = booking.objects.filter(booking_date=query_date)
        serialized = BookingSerializer(query_bookings,many=True)
        return Response({"status":"200","message":"success","data":serialized.data})

    def post(self,request):
        name = request.data.get('name','')
        license_plate_number = request.data['license_plate_number']
        booking_date = request.data['date']
        converted_date = datetime.fromisoformat(booking_date).date()
        query_bookings = booking.objects.filter(booking_date=booking_date)
        customer_obj,created = customer.objects.get_or_create(name=name,license_plate_number=license_plate_number)
        customer_query_filter = booking.objects.filter(customer=customer_obj,booking_date=booking_date)
  
        if len(list(customer_query_filter)) ==1:
            return Response(
                {
                    "status":"201",
                    "message":"Sorry, you have already made a booking",
                    "data":[]
                }
                )
        if len(list(query_bookings))==4:
                return Response(
                {
                    "status":"201",
                    "message":"No slots available for this day",
                    "data":[]
                }
                )


        if int((converted_date-datetime.now().date()).days)<2:
            
            return Response(
                {
                    "status":"201",
                    "message":"Bookings have to be made atleast 24 hours before the booking date",
                    "data":[]
                }
                )
        else:
            available_bays = ['Bay1','Bay2','Bay3','Bay4']
            for booking_made in query_bookings:
                if booking_made.bay_number in available_bays:
                    index = available_bays.index(booking_made.bay_number)
                    available_bays.pop(index)

            booking_to_create = booking.objects.create(customer=customer_obj,
                                                       bay_number=available_bays[0],
                                                       booking_date=booking_date)
            
            

        return Response({"status":"201","message":"success","data":[]})








