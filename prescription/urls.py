from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_px, name='order_px'),
]
