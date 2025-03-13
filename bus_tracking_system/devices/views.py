from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Device

class DeviceListView(ListView):
    model = Device
    template_name = 'devices/device_list.html'

class DeviceDetailView(DetailView):
    model = Device
    template_name = 'devices/device_detail.html'

class DeviceCreateView(CreateView):
    model = Device
    fields = ['imei', 'status']
    template_name = 'devices/device_form.html'
    success_url = reverse_lazy('device_list')

class DeviceUpdateView(UpdateView):
    model = Device
    fields = ['imei', 'status']
    template_name = 'devices/device_form.html'
    success_url = reverse_lazy('device_list')

class DeviceDeleteView(DeleteView):
    model = Device
    template_name = 'devices/device_confirm_delete.html'
    success_url = reverse_lazy('device_list')