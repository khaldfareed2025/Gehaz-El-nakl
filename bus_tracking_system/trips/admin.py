# trips/admin.py
from django.contrib import admin
from .models import Trip, TripLocation

class TripLocationInline(admin.TabularInline):
    model = TripLocation
    extra = 0

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('id', 'device', 'bus', 'driver', 'start_time', 'end_time', 'is_active')
    search_fields = ('device__imei', 'bus__plate_number', 'driver__name')
    inlines = [TripLocationInline]

@admin.register(TripLocation)
class TripLocationAdmin(admin.ModelAdmin):
    list_display = ('trip', 'latitude', 'longitude', 'speed', 'timestamp')
    search_fields = ('trip__id',)