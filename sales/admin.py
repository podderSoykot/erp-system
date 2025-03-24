from django.contrib import admin
from .models import Customer, Order, Invoice

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'quantity', 'order_date', 'status')
    search_fields = ('customer__first_name', 'customer__last_name', 'product__name')
    list_filter = ('status', 'order_date')

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('order', 'total_amount', 'date_issued', 'paid_status')
    search_fields = ('order__customer__first_name', 'order__customer__last_name')
    list_filter = ('paid_status', 'date_issued')
