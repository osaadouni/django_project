from django.db import models
from django.urls import reverse



class Department(models.Model):
  
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.name

    def get_absolute_url(self):
        return reverse("departments:department-edit", kwargs={'pk': self.pk})
     
    
    

