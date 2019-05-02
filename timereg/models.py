from django.db import models
from random import randint 
from django.urls import reverse
from django.contrib.auth.models import User 


class TimeReg(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
 
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE, verbose_name="Who's the client?")
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, verbose_name="What's the project?")
    activity = models.ForeignKey('activities.Activity', on_delete=models.CASCADE, verbose_name="What's the activity?")

    description = models.TextField()
 
    date = models.DateField()
    bill = models.BooleanField(default=True)
    time = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "Timereg #{}".format(self.pk)
   
    def get_absolute_url(self):
        return reverse("timereg:timereg-edit", kwargs={'pk': self.pk})



