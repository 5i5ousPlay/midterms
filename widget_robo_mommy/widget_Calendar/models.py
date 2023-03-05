from django.db import models


MODE_TYPES = (
    ('onsite', 'Onsite'),
    ('online', 'Online'),
    ('hybrid', 'Hybrid'),
)


class Location(models.Model):
    mode = models.CharField(max_length=6, choices=MODE_TYPES)
    venue = models.CharField(max_length=100)

    def __str__(self):
        return 'Mode: {} || Venue: {}'.format(self.mode, self.venue)


class Event(models.Model):
    target_datetime = models.CharField(max_length=20)
    activity = models.CharField(max_length=100)
    estimated_hours = models.FloatField()
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE
    )
    course = models.CharField(max_length=20)

    def __str__(self):
        return '{} on {}'.format(self.activity, self.target_datetime)
