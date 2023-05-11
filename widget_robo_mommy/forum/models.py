from django.db import models
from Dashboard.models import WidgetUser
# Create your models here.


class ForumPost(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    author = models.ForeignKey(WidgetUser, related_name='forumpost', on_delete=models.CASCADE, null=True)
    pub_datetime = models.DateTimeField(auto_now_add=True)


class Reply(models.Model):
    forum_post = models.ForeignKey(ForumPost, related_name='reply', on_delete=models.CASCADE, null=True)
    body = models.TextField(blank=True, null=True)
    author = models.ForeignKey(WidgetUser, on_delete=models.CASCADE, null=True)
    pub_datetime = models.DateTimeField(auto_now_add=True)
