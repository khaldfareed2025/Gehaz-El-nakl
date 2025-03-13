# trips/views.py

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views import View
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Trip, TripLocation
from devices.models import Device
from buses.models import Bus
from drivers.models import Driver


class TripListView(ListView):
    model = Trip
    template_name = 'trips/trip_list.html'
    context_object_name = 'trips'

    def get_queryset(self):
        return Trip.objects.order_by('-created_at')


class TripDetailView(DetailView):
    model = Trip
    template_name = 'trips/trip_detail.html'


class TripCreateView(CreateView):
    model = Trip
    fields = ['device', 'bus', 'driver']
    template_name = 'trips/trip_form.html'
    success_url = reverse_lazy('trip_list')

    def form_valid(self, form):
        # Get the selected device, bus, and driver
        device = form.cleaned_data['device']
        bus = form.cleaned_data['bus']
        driver = form.cleaned_data['driver']

        # Check if any of them are already in an active trip
        if Trip.objects.filter(device=device, is_active=True).exists():
            form.add_error('device', 'This device is already in use in an active trip.')
        if Trip.objects.filter(bus=bus, is_active=True).exists():
            form.add_error('bus', 'This bus is already in use in an active trip.')
        if Trip.objects.filter(driver=driver, is_active=True).exists():
            form.add_error('driver', 'This driver is already in use in an active trip.')

        # If there are any errors, return the form with errors
        if form.errors:
            return self.form_invalid(form)

        # If no errors, proceed with creating the trip
        response = super().form_valid(form)
        self.object.start_trip()  # Start the trip
        return response


# NEW TripUpdateView so “trip_update” route resolves
class TripUpdateView(UpdateView):
    model = Trip
    fields = ['device', 'bus', 'driver', 'start_time', 'end_time', 'is_active']
    template_name = 'trips/trip_form.html'
    success_url = reverse_lazy('trip_list')


class TripEndView(View):
    """
    Ends an active trip, sets end_time = now, is_active = False.
    """
    def get(self, request, pk):
        trip = get_object_or_404(Trip, pk=pk, is_active=True)
        trip.end_trip()
        return redirect('trip_list')


@api_view(['POST'])
def receive_location_update(request):
    """
    Receives GPS data from a SIM808 device as JSON:
    {
      "imei": "123456789012345",
      "latitude": 34.0522,
      "longitude": -118.2437,
      "speed": 50
    }
    """
    imei = request.data.get('imei')
    lat = request.data.get('latitude')
    lng = request.data.get('longitude')
    speed = request.data.get('speed')

    try:
        device = Device.objects.get(imei=imei, status='active')
        trip = Trip.objects.get(device=device, is_active=True)
        TripLocation.objects.create(
            trip=trip,
            latitude=lat,
            longitude=lng,
            speed=speed
        )
        return Response({"message": "Location saved."}, status=status.HTTP_201_CREATED)
    except Device.DoesNotExist:
        return Response({"error": "Device not found or not active."},
                        status=status.HTTP_404_NOT_FOUND)
    except Trip.DoesNotExist:
        return Response({"error": "No active trip found for this device."},
                        status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


def active_trips_data(request):
    """
    Returns a JSON of active trips with latest location.
    """
    active_trips = Trip.objects.filter(is_active=True).select_related('bus', 'driver', 'device')
    data = []
    for t in active_trips:
        last_loc = t.locations.order_by('-timestamp').first()
        if last_loc:
            data.append({
                'trip_id': t.id,
                'bus': t.bus.plate_number if t.bus else None,
                'driver': t.driver.name if t.driver else None,
                'imei': t.device.imei if t.device else None,
                'latitude': str(last_loc.latitude),
                'longitude': str(last_loc.longitude),
                'speed': str(last_loc.speed),
                'timestamp': last_loc.timestamp.strftime('%Y-%m-%d %H:%M:%S')
            })
    return JsonResponse(data, safe=False)