from django.db import models
from django.urls import reverse
from django.utils import timezone


class Employee(models.Model):
    """ Employee model class """
    name = models.CharField(max_length=120)
    department = models.CharField(max_length=320)
    position = models.CharField(max_length=320)
    started_work = models.DateField(default=timezone.now)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    github_link = models.CharField(max_length=240, unique=True,
                                   blank=True, null=True)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def get_delete_url(self):
        return reverse('delete_employee', args={'pk': self.id})

    def __str__(self):
        return self.name
