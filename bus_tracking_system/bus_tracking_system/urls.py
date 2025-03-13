from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Each app’s URLs
    path('devices/', include('devices.urls')),
    path('buses/', include('buses.urls')),
    path('drivers/', include('drivers.urls')),
    path('trips/', include('trips.urls')),
]
