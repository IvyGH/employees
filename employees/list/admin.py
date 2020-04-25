from django.contrib import admin

from .models import Employee


@admin.register(Employee)
class EmployeeModelAdmin(admin.ModelAdmin):
    """ Employee model admin """
    list_display = ('name', 'department', 'position',
                    'started_work', 'left_work', 'date_of_birth', 'phone_number', 'email', 'github_link', 'slug')
