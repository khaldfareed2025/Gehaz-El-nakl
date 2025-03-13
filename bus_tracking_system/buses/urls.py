# Corrected URL pattern in buses/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.BusListView.as_view(), name='bus_list'),
    path('create/', views.BusCreateView.as_view(), name='bus_create'),
    path('<int:pk>/', views.BusDetailView.as_view(), name='bus_detail'),
    path('<int:pk>/update/', views.BusUpdateView.as_view(), name='bus_update'),
    path('<int:pk>/delete/', views.BusDeleteView.as_view(), name='bus_delete'),
]