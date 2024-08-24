from rest_framework import serializers
from busapp.models import BusDetails

class BusDetailsSerializer(serializers.ModelSerializer):
    class Meta:
         model=BusDetails
         fields=['name','bus_no','total_seats','bus_type','start_point','end_point','start_time','price']