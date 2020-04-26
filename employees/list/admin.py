from django.contrib import admin

from .models import Employee


@admin.register(Employee)
class EmployeeModelAdmin(admin.ModelAdmin):
    """ Employee model admin """
    list_display = ('name', 'department', 'position',
                    'started_work', 'date_of_birth',
                    'email', 'github_link')
