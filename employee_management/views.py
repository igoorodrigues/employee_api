from rest_framework import viewsets
from employee_management.models import Employee
from employee_management.serializer import EmployeeSerializer

class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer