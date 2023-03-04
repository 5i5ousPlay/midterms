from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# temporary user model for testing
class WidgetUser(User):
    pass

class ForumPost(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    author = models.ForeignKey(WidgetUser, related_name='forumpost', on_delete=models.CASCADE, null=True)
    pub_datetime = models.DateTimeField(auto_now_add=True)

class Reply(models.Model):
    body = models.TextField(blank=True, null=True)
    author = models.ForeignKey(WidgetUser, related_name='reply', on_delete=models.CASCADE, null=True)
    pub_datetime = models.DateTimeField(auto_now_add=True)

