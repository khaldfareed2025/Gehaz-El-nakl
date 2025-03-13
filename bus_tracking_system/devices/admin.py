from django.contrib import admin

# Register your models here.
from .models import Device

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('imei', 'status', 'created_at')
    search_fields = ('imei',)