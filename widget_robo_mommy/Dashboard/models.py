from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    dept_name = models.CharField(max_length=50)
    home_unit = models.CharField(max_length=100)

class WidgetUser(User):
    pass

