from django.contrib import admin

from .models import Department


class DepartmentAdmin(admin.ModelAdmin):
    model = Department

    list_display = ('dept_name', 'home_unit')

    search_fields = ('dept_name', 'home_unit')


admin.site.register(Department, DepartmentAdmin)
