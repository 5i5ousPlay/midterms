from django.contrib import admin
from .models import ForumPost, Reply, WidgetUser

# Register your models here.
admin.site.register(ForumPost)
admin.site.register(Reply)
admin.site.register(WidgetUser)
