from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from employees.models import Employee


class EmployeeList(ListView):
    model = Employee
    ordering = ['-pk']
    #paginate_by = 5
    #template_name = 'employees/employees.html' # to override the default template 


class EmployeeView(DetailView):
    model = Employee


class EmployeeCreate(CreateView):
    model = Employee
    fields = ['name', 'pages']
    template_name = 'employees/employee_form_add.html'
    success_url = reverse_lazy('employees:employee-list')

class EmployeeUpdate(UpdateView):
    model = Employee
    fields = ['name', 'pages']
    template_name = 'employees/employee_form_edit.html'
    success_url = reverse_lazy('employees:employee-list')
 
class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('employees:employee-list')



class AboutView(TemplateView):
    template_name = 'about.html' 
