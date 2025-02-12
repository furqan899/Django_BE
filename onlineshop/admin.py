from django.contrib import admin
from .models import Category, Product, Order

# Custom admin configurations
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at', 'updated_at']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'category', 'image', 'created_at', 'updated_at']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'customer_email', 'product', 'quantity', 'created_at', 'updated_at']

# Registering models with their custom admin configurations
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
