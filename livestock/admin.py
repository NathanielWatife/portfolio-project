"""Module for registering models with the Django admin site."""
from django.contrib import admin
from .models import Livestock, HealthRecord

# Register your models here.
admin.site.register(Livestock)
admin.site.register(HealthRecord)