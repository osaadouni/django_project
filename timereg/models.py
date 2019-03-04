from django.db import models
from random import randint 
from django.urls import reverse

from clients.models import Client
from projects.models import Project
from activities.models import Activity

     
class TimeReg(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Who's the client?")
    timereg = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="What's the timereg?")
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, verbose_name="What's the activity?")
    description = models.TextField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.description
   
    def get_absolute_url(self):
        return reverse("timereg:timereg-edit", kwargs={'pk': self.pk})


