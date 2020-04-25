from django.db import models
from django.urls import reverse
from django.utils import timezone


class Employee(models.Model):
    """ Employee model class """
    name = models.CharField(max_length=120)
    department = models.CharField(max_length=320)
    position = models.CharField(max_length=320)
    started_work = models.DateField(default=timezone.now)
    left_work = models.DateField(blank=True, null=True)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    github_link = models.CharField(max_length=240, unique=True,
                                   blank=True, null=True)
    slug = models.SlugField(max_length=120, unique=True)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def get_absolute_url(self):
        return reverse('add_employee', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name
