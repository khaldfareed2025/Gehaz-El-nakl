# trips/models.py
from django.db import models
from django.utils import timezone
from devices.models import Device
from buses.models import Bus
from drivers.models import Driver

class Trip(models.Model):
    device = models.ForeignKey(Device, on_delete=models.SET_NULL, null=True)
    bus = models.ForeignKey(Bus, on_delete=models.SET_NULL, null=True)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Trip #{self.id} - {self.bus} | {self.driver} | {self.device}"

    def start_trip(self):
        self.start_time = timezone.now()
        self.is_active = True
        self.save()

    def end_trip(self):
        self.end_time = timezone.now()
        self.is_active = False
        self.save()

class TripLocation(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='locations')

    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    speed = models.DecimalField(max_digits=5, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Location for Trip #{self.trip.id} - {self.timestamp}"