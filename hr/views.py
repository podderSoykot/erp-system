from django.shortcuts import render  # Fixed missing import
from .models import Employee, Salary, Attendance

def employee_list(request):
    employees = Employee.objects.all().order_by('-date_joined')  # Order by latest
    return render(request, 'hr/employee_list.html', {'employees': employees})

def salary_list(request):
    salaries = Salary.objects.select_related('employee').order_by('-date_issued')  
    return render(request, 'hr/salary_list.html', {'salaries': salaries})

def attendance_list(request):
    attendance = Attendance.objects.select_related('employee').order_by('-date')  
    return render(request, 'hr/attendance_list.html', {'attendance': attendance})

