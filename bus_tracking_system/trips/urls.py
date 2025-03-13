# trips/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.TripListView.as_view(), name='trip_list'),
    path('create/', views.TripCreateView.as_view(), name='trip_create'),

    # path for “Edit” link in trip_list.html or trip_detail.html
    path('<int:pk>/update/', views.TripUpdateView.as_view(), name='trip_update'),

    path('<int:pk>/', views.TripDetailView.as_view(), name='trip_detail'),
    path('<int:pk>/end/', views.TripEndView.as_view(), name='trip_end'),

    # Optional: “trip_delete” route, location endpoints, etc.
    # path('<int:pk>/delete/', views.TripDeleteView.as_view(), name='trip_delete'),
    path('receive-location/', views.receive_location_update, name='receive_location'),
    path('active-data/', views.active_trips_data, name='active_trips_data'),
]