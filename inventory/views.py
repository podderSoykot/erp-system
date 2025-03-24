from django.shortcuts import render
from .models import Product, Stock

def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})
def stock_list(request):
    stocks = Stock.objects.all()
    return render(request, 'inventory/stock_list.html', {'stocks': stocks})
