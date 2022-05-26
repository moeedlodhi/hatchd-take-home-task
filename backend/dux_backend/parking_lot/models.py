from django.db import models
from datetime import datetime
# Create your models here.

PARKING_BAYS = [
    ('Bay1','Bay1'),
    ('Bay2','Bay2'),
    ('Bay3','Bay3'),
    ('Bay4','Bay4')
]

class customer(models.Model):
    name = models.CharField(max_length=500, blank=True)
    license_plate_number = models.CharField(max_length=500, unique=True)

class booking(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    bay_number = models.CharField(max_length=264, choices=PARKING_BAYS)
    booking_date = models.DateField()

    class Meta:
        unique_together = ('bay_number','booking_date')

    

