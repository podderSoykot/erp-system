"""
URL configuration for erp_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from inventory import views as inventory_views
from hr import views as hr_views
from sales import views as sales_views
from django.conf import settings
from django.conf.urls.static import static
from sales.views import checkout

# Define a homepage view
def home(request):
    return render(request, 'home.html')  

urlpatterns = [
    path('admin/', admin.site.urls),

    # Homepage
    path('', home, name='home'),

    # Inventory URLs
    path('inventory/products/', inventory_views.product_list, name='product_list'),
    path('inventory/stocks/', inventory_views.stock_list, name='stock_list'),

    # HR Management URLs
    path('hr/employees/', hr_views.employee_list, name='employee_list'),
    path('hr/salaries/', hr_views.salary_list, name='salary_list'),
    path('hr/attendance/', hr_views.attendance_list, name='attendance_list'),

    # Sales & CRM URLs
    path('sales/customers/', sales_views.customer_list, name='customer_list'),
    path('sales/orders/', sales_views.order_list, name='order_list'),
    path('sales/invoices/', sales_views.invoice_list, name='invoice_list'),

    # Checkout & Order Confirmation
    path('sales/checkout/<int:product_id>/', sales_views.checkout, name='checkout'),
    path('sales/order-confirmation/<int:order_id>/', sales_views.order_confirmation, name='order_confirmation'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
