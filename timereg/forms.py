from django import forms

from .models import TimeReg
from clients.models import Client
from projects.models import Project
from activities.models import Activity

class TimeRegForm(forms.ModelForm):
    client =  forms.ModelChoiceField(queryset=Client.objects.order_by('name'), empty_label="-- (Select Client) -- ")
    project =  forms.ModelChoiceField(queryset=Project.objects.order_by('name'), empty_label="-- (Select Project) -- ")

    class Meta:
        model = TimeReg
        fields = ['client',  'project', 'activity', 'description', 'date']

