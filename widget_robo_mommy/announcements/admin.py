from django.contrib import admin
from .models import Announcement, Reaction

class AnnouncementAdmin(admin.ModelAdmin):
    model = Announcement

class ReactionAdmin(admin.ModelAdmin):
    model = Reaction

# Register your models here.
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Reaction, ReactionAdmin)