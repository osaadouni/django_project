from django.db import models
from django.urls import reverse
from django.utils import timezone


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)

    #class Meta:
    #    db_table = 'employee'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('employees:employee-edit', kwargs={'pk': self.pk})

