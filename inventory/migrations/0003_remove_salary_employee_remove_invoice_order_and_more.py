# Generated by Django 5.1.7 on 2025-03-21 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_employee_product_image_alter_stock_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salary',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='order',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Salary',
        ),
        migrations.DeleteModel(
            name='Invoice',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
