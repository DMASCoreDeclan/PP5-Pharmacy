from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/', views.delete_product, name='delete_product'),
    path('delete_products/', views.delete_products, name='delete_products'),
    path('edit_products/', views.edit_products, name='edit_products'),
    
]
