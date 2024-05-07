from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_px, name='order_px'),
    path('px_admin', views.px_admin, name='px_admin'),
    path('edit_px_status/<int:px_id>', views.edit_px_status, name='edit_px_status'),
]
