from django.test import TestCase
from rest_framework.test import APITestCase
from .models import customer,booking
from datetime import datetime

class BasicTest(APITestCase):
    
    def test_get_all_booking(self):

        response = self.client.get('/parking/parkinglot/?=2022-05-28')
        self.assertEqual(response.status_code, 200)


    def test_single_booking(self):
        data={
            
            "name":"ed",
            "license_plate_number":"ed52",
            "date":"2022-05-28"

        }
        response = self.client.post('/parking/parkinglot/',data)
        self.assertEqual(response.status_code, 200)

    def test_already_single_booking(self):
        customer_to_create = customer.objects.create(name='moeed', license_plate_number="moeed123")
        booking_to_create = booking.objects.create(customer=customer_to_create,
                                                       bay_number='Bay1',
                                                       booking_date="2022-05-28")
        data={
            
            "name":"moeed",
            "license_plate_number":"moeed123",
            "date":"2022-05-28"

        }
        response = self.client.post('/parking/parkinglot/',data)
        self.assertEqual(response.status_code, 200)

    def test_all_slots_booked(self):
        customer1 = customer.objects.create(name='moeed', license_plate_number="moeed1")
        customer2 = customer.objects.create(name='moeed', license_plate_number="moeed2")
        customer3 = customer.objects.create(name='moeed', license_plate_number="moeed3")
        customer4 = customer.objects.create(name='moeed', license_plate_number="moeed4")

        booking1 = booking.objects.create(customer=customer1,bay_number='Bay1',booking_date="2022-05-28")
        booking2 = booking.objects.create(customer=customer2,bay_number='Bay2',booking_date="2022-05-28")
        booking3 = booking.objects.create(customer=customer3,bay_number='Bay3',booking_date="2022-05-28")
        booking4 = booking.objects.create(customer=customer4,bay_number='Bay4',booking_date="2022-05-28")

        data={
            
            "name":"moeed",
            "license_plate_number":"moeed123",
            "date":"2022-05-28"

        }
        response = self.client.post('/parking/parkinglot/',data)
        self.assertEqual(response.status_code, 200)

    def test_booking_date(self):

        data={
            
            "name":"moeed",
            "license_plate_number":"moeed123",
            "date":f"{datetime.now().date()}"

        }
        response = self.client.post('/parking/parkinglot/',data)
        self.assertEqual(response.status_code, 200)
        





