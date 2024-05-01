from django.contrib import admin
from django.contrib.auth.models import User
from .models import Prescription

# Register your models here.

class PrescriptionAdmin(admin.ModelAdmin):
    fieds = (
        # 'user', 
        'full_name', 
        'email', 
        'phone_number', 
        'date_sent', 
        'date_required', 
        'dr_full_name', 
        'px_image', 
        'date_sent', 
        'px_status', 
        'px_delivery', 
        )

    list_display = (
        'full_name', 
        'email', 
        'phone_number', 
        'date_sent', 
        'date_required', 
        'dr_full_name', 
        'px_image', 
        'date_sent', 
        'px_status', 
        'px_delivery', 
        )

    ordering = ('px_status', )

admin.site.register(Prescription, PrescriptionAdmin)