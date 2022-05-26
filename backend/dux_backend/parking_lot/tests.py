from django.test import TestCase
from rest_framework.test import APITestCase
from .models import customer,booking
from datetime import datetime,date,timedelta

class BasicTest(APITestCase):
    def test_get_all_booking(self):
        booking_date = date.today() + timedelta(days=10)
        response = self.client.get(f'/parking/parkinglot/?=${booking_date}')
        self.assertEqual(response.json()['message'], "success")


    def test_single_booking(self):
        booking_date = date.today() + timedelta(days=10)
        data={
            
            "name":"ed",
            "license_plate_number":"ed52",
            "date":f"{booking_date}"

        }
        response = self.client.post('/parking/parkinglot/',data)
        self.assertEqual(response.status_code, 200)

    def test_already_single_booking(self):
        booking_date = date.today() + timedelta(days=10)
        customer_to_create = customer.objects.create(name='moeed', license_plate_number="moeed123")
        booking_to_create = booking.objects.create(customer=customer_to_create,
                                                       bay_number='Bay1',
                                                       booking_date=f"{booking_date}")
        data={
            
            "name":"moeed",
            "license_plate_number":"moeed123",
            "date":f"{booking_date}"

        }
        response = self.client.post('/parking/parkinglot/',data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], "Sorry, you have already made a booking")

    def test_all_slots_booked(self):
        booking_date = date.today() + timedelta(days=10)
        customer1 = customer.objects.create(name='moeed', license_plate_number="moeed1")
        customer2 = customer.objects.create(name='moeed', license_plate_number="moeed2")
        customer3 = customer.objects.create(name='moeed', license_plate_number="moeed3")
        customer4 = customer.objects.create(name='moeed', license_plate_number="moeed4")

        booking1 = booking.objects.create(customer=customer1,bay_number='Bay1',booking_date=f"{booking_date}")
        booking2 = booking.objects.create(customer=customer2,bay_number='Bay2',booking_date=f"{booking_date}")
        booking3 = booking.objects.create(customer=customer3,bay_number='Bay3',booking_date=f"{booking_date}")
        booking4 = booking.objects.create(customer=customer4,bay_number='Bay4',booking_date=f"{booking_date}")

        data={
            
            "name":"moeed",
            "license_plate_number":"moeed123",
            "date":f"{booking_date}"

        }
        response = self.client.post('/parking/parkinglot/',data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], "No slots available for this day")

    def test_booking_date(self):

        data={
            
            "name":"moeed",
            "license_plate_number":"moeed123",
            "date":f"{datetime.now().date()}"

        }
        response = self.client.post('/parking/parkinglot/',data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], "Bookings have to be made atleast 24 hours before the booking date")
        





