from django.db import models
from django.urls import reverse 
from django.utils import timezone

class Book(models.Model):
    name  = models.CharField(max_length=200)
    pages = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return reverse('books:book-edit', kwargs={'pk': self.pk})
        # works as well: return reverse('book-edit', args=(self.pk,))
 
