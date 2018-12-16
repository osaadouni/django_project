from django.forms import ModelForm

from employees.models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'phone']



