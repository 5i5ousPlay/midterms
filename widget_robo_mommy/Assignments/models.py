from django.db import models
from django.urls import reverse


class Course(models.Model):
    code = models.CharField(max_length=10, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    section = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        return self.code + '-' + self.section


class Assignment(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    perfect_score = models.IntegerField(blank=True, null=True)
    passing_score = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.passing_score = int(self.perfect_score * 0.60)
        super(Assignment, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('assignments:assignments-item', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('assignments:assignments-edit', kwargs={'pk': self.pk})
