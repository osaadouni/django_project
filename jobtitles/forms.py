from django import forms

from jobtitles.models import JobTitle

class JobTitleForm(forms.ModelForm):
    class Meta:
        model = JobTitle
        fields = ['name']


