from django.contrib import admin
from .models import Product, Stock

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'supplier', 'received_at')
    search_fields = ('product__name', 'supplier')
    list_filter = ('received_at',)



# # # Register models
# admin.site.register(Product, ProductAdmin)
# admin.site.register(Stock, StockAdmin)

