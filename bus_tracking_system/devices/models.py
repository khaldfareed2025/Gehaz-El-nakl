from django.db import models

# Create your models here.
class Device(models.Model):
    imei = models.CharField(max_length=50, unique=True)
    STATUS_CHOICES = (
    ('active', 'Active'),
    ('inactive', 'Inactive'),
    ('maintenance', 'Maintenance'),
    )
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='inactive')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Device (IMEI: {self.imei}, Status: {self.status})"