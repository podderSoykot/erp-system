# Generated by Django 5.1.7 on 2025-03-22 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0002_alter_employee_date_joined_alter_employee_department_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salary',
            name='date_issued',
            field=models.DateField(),
        ),
    ]
