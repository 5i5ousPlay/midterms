from django.db import models
from Dashboard.models import WidgetUser

class Announcement(models.Model):
    title = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    author = models.ForeignKey(WidgetUser, on_delete=models.CASCADE, null=True)
    pub_datetime = models.DateTimeField(null=True)

class Reaction(models.Model):
    LIKE = 'Like'
    LOVE = 'Love'
    ANGRY = 'Angry'
    REACTION_CHOICES = [
        (LIKE, 'Like'),
        (LOVE, 'Love'),
        (ANGRY, 'Angry'),
    ]

    name = models.CharField(max_length=5, default=LIKE, null=True, blank=True)
    tally = models.IntegerField(default=0 ,null=True, blank=True)
    announcement = models.ForeignKey(Announcement, related_name="react", on_delete=models.CASCADE, null=True)

# Create your models here.
