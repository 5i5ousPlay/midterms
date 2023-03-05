from django.contrib import admin
from .models import Location, Event


class LocationAdmin(admin.ModelAdmin):
    model = Location


class EventAdmin(admin.ModelAdmin):
    model = Event


admin.site.register(Location, LocationAdmin)
admin.site.register(Event, EventAdmin)
