from django.contrib import admin
from .models import Product, Category, ProductBundle

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'category',
        'has_sizes',
        'size',
        'price',
        'rating',
        'thumbnail',
    )

    ordering = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductBundleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'category',
        'has_sizes',
        'size',
        'price',
        'rating',
        'thumbnail',
    )

    ordering = ('name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductBundle, ProductBundleAdmin)