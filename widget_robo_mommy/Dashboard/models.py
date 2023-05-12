from django.db import models
from django.urls import reverse


class Department(models.Model):
    dept_name = models.CharField(max_length=50)
    home_unit = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.dept_name)


class WidgetUser(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, related_name="department", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.last_name + ', ' + self.first_name)

    def get_absolute_url(self):
        return reverse('widgetuser-detail', kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return reverse('widgetuser-add', kwargs={'pk': self.pk})
