from django.contrib import admin
from .models import Employee, Salary, Attendance

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'position', 'date_joined')
    search_fields = ('name', 'department')
    ordering = ('-date_joined',)
    list_per_page = 20  # Pagination

class SalaryAdmin(admin.ModelAdmin):
    list_display = ('employee', 'amount', 'date_issued')
    list_filter = ('date_issued',)
    search_fields = ('employee__name',)
    ordering = ('-date_issued',)

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'status')
    list_filter = ('status', 'date')
    search_fields = ('employee__name',)
    ordering = ('-date',)

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Salary, SalaryAdmin)
admin.site.register(Attendance, AttendanceAdmin)

