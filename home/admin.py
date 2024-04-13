from django.contrib import admin
from .models import CommunicationType, CommunicationStatus, CommunicationContent


class StatusAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'status',
    )

    ordering = ('id',)


class CommunicationTypeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'friendly_name',
        'name',
    )

    ordering = ('name',)


class CommunicationContentAdmin(admin.ModelAdmin):
    list_display = (
        'status', 
        'author',
        'content_type',  
        'title', 
        'slug', 
        'created_on', 
        'updated_on', 
        'content', 
        'image', 
    )

    fields = (
        'content_type', 
        'status', 
        'author', 
        'title', 
        'slug', 
        'content', 
        'image', 
    )

    ordering = ('-created_on',)


# Register your models here.
admin.site.register(CommunicationStatus, StatusAdmin)
admin.site.register(CommunicationType, CommunicationTypeAdmin)
admin.site.register(CommunicationContent, CommunicationContentAdmin)

