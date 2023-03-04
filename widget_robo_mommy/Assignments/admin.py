from django.contrib import admin
from .models import Subject, IndexCard

class AssignmentAdmin(admin.ModelAdmin):
    model = Assignment

class CourseAdmin(admin.ModelAdmin):
    model = Course

admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Course, CourseAdmin)