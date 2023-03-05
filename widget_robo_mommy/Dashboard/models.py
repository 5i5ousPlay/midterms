from django.db import models


class Department(models.Model):
    dept_name = models.CharField(max_length=50)
    home_unit = models.CharField(max_length=100)


class WidgetUser(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)