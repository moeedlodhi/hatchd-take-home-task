from rest_framework import serializers
from .models import booking,customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    class Meta:
        model = booking
        fields = '__all__'
