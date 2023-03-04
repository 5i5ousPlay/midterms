from django.db import models


class Department(models.Model):
    dept_name = models.CharField(max_length=50)
    home_unit = models.CharField(max_length=100)
