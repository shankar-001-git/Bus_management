from django.db import models

class BusDetails(models.Model):
    name = models.CharField(max_length=100)
    bus_no = models.CharField(max_length=100)
    total_seats = models.IntegerField()
    bus_type = models.CharField(max_length=100)
    start_point = models.CharField(max_length=100)
    end_point = models.CharField(max_length=100)
    start_time = models.TimeField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='image',blank=True,null=True)


