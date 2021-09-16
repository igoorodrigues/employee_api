from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=70)
    department = models.CharField(max_length=30)

    def tuple(self):
        return self.name, self.email, self.department
