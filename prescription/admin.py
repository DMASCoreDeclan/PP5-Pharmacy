from django.contrib import admin
from django.contrib.auth.models import User
from .models import Prescription

# Register your models here.

class PrescriptionAdmin(admin.ModelAdmin):
    # list_display = (
    #     'dr_full_name',
    #     'px_image',
    #     'date_sent',
    #     'px_status',
    #     'px_delivery',
    #     # 'default_phone_number',
    #     # 'default_street_address1',
    #     # 'default_street_address2',
    #     # 'default_town_or_city',
    #     # 'default_postcode',
    #     # 'default_county',
    #     # 'default_country',
    # )

    # exclude = (
    #     'user',
    # )

    ordering = ('px_status',)


admin.site.register(Prescription, PrescriptionAdmin)