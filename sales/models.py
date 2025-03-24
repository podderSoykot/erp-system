from django.db import models
from inventory.models import Product  # Import Product from inventory
from django.contrib.auth.models import User


class Customer(models.Model):
    """Represents a customer in the system."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer", null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Order(models.Model):
    """Represents an order placed by a customer."""
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Processing", "Processing"),
        ("Shipped", "Shipped"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")

    def __str__(self):
        return f"Order #{self.id} - {self.product.name} by {self.customer.first_name} ({self.status})"

class Invoice(models.Model):
    """Represents an invoice for an order."""
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="invoice")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_issued = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    paid_status = models.BooleanField(default=False)

    def __str__(self):
        return f"Invoice #{self.id} for Order #{self.order.id} - ${self.total_amount} ({'Paid' if self.paid_status else 'Unpaid'})"

class Checkout(models.Model):
    """Handles temporary checkout records before finalizing an order."""
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Checkout by {self.customer.first_name} ({'Completed' if self.completed else 'Pending'})"
