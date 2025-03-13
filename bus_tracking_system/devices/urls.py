# bus_tracking_system/devices/urls.py
# Change "int:pk/" to "<int:pk>/".
from django.urls import path
from . import views

urlpatterns = [
    path('', views.DeviceListView.as_view(), name='device_list'),
    path('create/', views.DeviceCreateView.as_view(), name='device_create'),
    path('<int:pk>/', views.DeviceDetailView.as_view(), name='device_detail'),
    path('<int:pk>/update/', views.DeviceUpdateView.as_view(), name='device_update'),
    path('<int:pk>/delete/', views.DeviceDeleteView.as_view(), name='device_delete'),
]