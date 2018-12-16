from django.db import models
from django.urls import reverse
from django.utils import timezone


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #class Meta:
    #    db_table = 'employee'
    
    def __str__(self):
        return ' '.join((self.first_name, self.last_name))
    
    def get_absolute_url(self):
        return reverse('employees:employee-edit', kwargs={'pk': self.pk})

