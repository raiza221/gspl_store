from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at', 'updated_at')
    search_fields = ['name']
    list_filter = ['created_at', 'updated_at']
    ordering = ['created_at']

admin.site.register(Product, ProductAdmin)
