from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Customer, Order, Invoice
from inventory.models import Product

def customer_list(request):
    """Displays a list of all customers."""
    customers = Customer.objects.all()
    return render(request, 'sales/customer_list.html', {'customers': customers})

def order_list(request):
    """Displays a list of all orders."""
    orders = Order.objects.all()
    return render(request, 'sales/order_list.html', {'orders': orders})

def invoice_list(request):
    """Displays a list of all invoices."""
    invoices = Invoice.objects.all()
    return render(request, 'sales/invoice_list.html', {'invoices': invoices})

@login_required
def checkout(request, product_id):
    """Handles order creation when a user proceeds to checkout."""
    product = get_object_or_404(Product, id=product_id)
    customer = get_object_or_404(Customer, user=request.user)

    # Creating the order with default quantity = 1
    order = Order.objects.create(customer=customer, product=product, quantity=1)

    messages.success(request, "Order placed successfully!")
    return redirect('order_confirmation', order_id=order.id)

@login_required
def order_confirmation(request, order_id):
    """Displays order confirmation page."""
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'sales/order_confirmation.html', {'order': order})

def checkout(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'sales/checkout.html', {'product': product})
