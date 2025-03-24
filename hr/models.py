from django.db import models
from django.utils import timezone

class Employee(models.Model):
    DEPARTMENT_CHOICES = [
        ('HR', 'Human Resources'),
        ('IT', 'Information Technology'),
        ('FIN', 'Finance'),
        ('MKT', 'Marketing'),
        ('SALES', 'Sales'),
    ]
    name = models.CharField(max_length=255)  # Ensure this field is defined
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100, default="Employee")
    date_joined = models.DateField()
    photo = models.ImageField(upload_to='employee_photos/', blank=True, null=True)

    def __str__(self):
        return self.name

class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_issued = models.DateField()

    def __str__(self):
        return f"{self.employee.name} - ${self.amount:.2f}"

class Attendance(models.Model):
    STATUS_CHOICES = [('P', 'Present'), ('A', 'Absent')]
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.employee.name} - {self.get_status_display()} on {self.date}"
