from django import forms

from employees.models import Employee
from jobtitles.models import JobTitle

class EmployeeForm(forms.ModelForm):
    job_title =  forms.ModelChoiceField(queryset=JobTitle.objects.all(), empty_label="-- (Select Job Title) -- ")
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'phone', 'job_title', 'address', 'state', 'zipcode', 'city', 'country', 'is_admin',  'picture']
        widgets = {
            'address': forms.Textarea(attrs={'rows':4, 'cols': 15}),
        }


