from django.contrib import admin
from employee_management.models import Employee

class Employees(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'department')
    list_display_links = ('id', 'name', 'email', 'department')
    search_fields = ('name',)

admin.site.register(Employee,Employees)