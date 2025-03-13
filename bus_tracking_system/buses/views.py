from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Bus

class BusListView(ListView):
    model = Bus
    template_name = 'buses/bus_list.html'
    context_object_name = 'buses'

class BusDetailView(DetailView):
    model = Bus
    template_name = 'buses/bus_detail.html'

class BusCreateView(CreateView):
    model = Bus
    fields = ['plate_number', 'model', 'capacity']
    template_name = 'buses/bus_form.html'
    success_url = reverse_lazy('bus_list')

class BusUpdateView(UpdateView):
    model = Bus
    fields = ['plate_number', 'model', 'capacity']
    template_name = 'buses/bus_form.html'
    success_url = reverse_lazy('bus_list')

class BusDeleteView(DeleteView):
    model = Bus
    template_name = 'buses/bus_confirm_delete.html'
    success_url = reverse_lazy('bus_list')