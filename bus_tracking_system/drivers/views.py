from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Driver

class DriverListView(ListView):
    model = Driver
    template_name = 'drivers/driver_list.html'
    context_object_name = 'drivers'

class DriverDetailView(DetailView):
    model = Driver
    template_name = 'drivers/driver_detail.html'

class DriverCreateView(CreateView):
    model = Driver
    fields = ['name', 'license_number', 'phone_number']
    template_name = 'drivers/driver_form.html'
    success_url = reverse_lazy('driver_list')

class DriverUpdateView(UpdateView):
    model = Driver
    fields = ['name', 'license_number', 'phone_number']
    template_name = 'drivers/driver_form.html'
    success_url = reverse_lazy('driver_list')

class DriverDeleteView(DeleteView):
    model = Driver
    template_name = 'drivers/driver_confirm_delete.html'
    success_url = reverse_lazy('driver_list')