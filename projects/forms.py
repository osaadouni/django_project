from django import forms

from projects.models import Project, ProjectState, ProjectPhase
from clients.models import Client
from employees.models import Employee

class ProjectForm(forms.ModelForm):
    client =  forms.ModelChoiceField(queryset=Client.objects.order_by('name'), empty_label="-- (Select Client) -- ")
    state =  forms.ModelChoiceField(queryset=ProjectState.objects.order_by('name'), empty_label="-- (Select State) -- ")
    phase =  forms.ModelChoiceField(queryset=ProjectPhase.objects.order_by('name'), empty_label="-- (Select Phase) -- ")
    manager =  forms.ModelChoiceField(queryset=Employee.objects.order_by('last_name'), empty_label="-- (Select Manager) -- ")

    class Meta:
        model = Project
        fields = ['client',  'price_type', 'description', 'manager', 'budgetted_hours', 'state', 'phase', 'client_ref_number', 'invoice_number', 'kind']


class ProjectStateForm(forms.ModelForm):
    class Meta:
        model = ProjectState
        fields = ['name']


class ProjectPhaseForm(forms.ModelForm):
    class Meta:
        model = ProjectPhase
        fields = ['name']
