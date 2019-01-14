from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator 


from employees.models import Employee
from .forms import EmployeeForm


class EmployeeList(ListView):
    model = Employee  # same as Employee.objects.all() 
    #queryset = Employee.objects.order_by('-pk')
    ordering = ['-pk']
    paginate_by = 5
    #paginator_class = Paginator 
    template_name = 'employees/employee_list.html' # to override the default template 
    context_object_name = "employee_list"
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        employee_list = Employee.objects.order_by('-pk')
        paginator = Paginator(employee_list, self.paginate_by)   

        page = self.request.GET.get('page')
        
        employees = paginator.get_page(page)

        context['object_list'] = employees  
        return context  


class EmployeeView(DetailView):
    model = Employee


class EmployeeCreate(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employees/employee_create_form.html'
    success_url = reverse_lazy('employees:employee-list')

class EmployeeUpdate(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employees/employee_edit_form.html'
    success_url = reverse_lazy('employees:employee-list')
 
class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('employees:employee-list')



class AboutView(TemplateView):
    template_name = 'about.html' 
