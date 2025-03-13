from django.contrib import admin
from .models import Bus

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ('plate_number', 'model', 'capacity', 'created_at')
    search_fields = ('plate_number', 'model')