from django.contrib import admin

from .models import Product, Photo


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'Name',
        'Body',
        'Type',
        'Available',
        'Price',
        'Quantity',
        'Created_on',
    )
    list_filter = ('Available', 'Created_on')


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'Color', 'product', 'Image', 'Cover')
    list_filter = ('product', 'Cover')
