from django import forms

from departments.models import Department

class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ('name',)
