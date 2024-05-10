from django.contrib import admin
from .models import CommunicationType, CommunicationStatus
from .models import CommunicationContent, Service
from django_summernote.admin import SummernoteModelAdmin


@admin.register(CommunicationStatus)
class StatusAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'status',
    )

    ordering = ('id',)


@admin.register(CommunicationType)
class CommunicationTypeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'friendly_name',
        'name',
    )

    ordering = ('name',)


@admin.register(CommunicationContent)
class CommunicationContentAdmin(SummernoteModelAdmin):
    list_display = (
        'status',
        'author',
        'short_description',
        'title',
        'slug',
        'created_on',
        'updated_on',
        'image',
    )

    fields = (
        'status',
        'author',
        'content_type',
        'title',
        'slug',
        'content',
        'image',
    )
    list_filter = ("content_type",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Service)
class ServiceAdmin(SummernoteModelAdmin):
    list_display = (
        'author',
        'title',
        'icon',
        'content',
    )
    fields = (
        'author',
        'title',
        'icon',
        'content',
    )
    ordering = ('title',)
