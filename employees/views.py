from django.shortcuts import render, redirect, get_object_or_404


from employees.forms import EmployeeForm
from employees.models import Employee

def employee_list(request, template_name='employees/employee_list.html'):
    employees = Employee.objects.all()
    context = { 'object_list': employees }
    return render(request, template_name, context)


def employee_view(request, pk, template_name='employees/employee_detail.html'):
    employee = get_object_or_404(Employee, pk=pk)
    context = { 'object': employee)
    return rendder(request, template_name, context)

def employee_create(request, template_name='employees/employee_form.html'):
    form = EmployeeForm(request.POST or None)
    if form.is_valid(): 
        form.save()
        return redirect('employees:employee-list')
    context = {'form': form, 'title': 'Add Employee'}
    return render(request, template_name, context)


def employee_update(request, pk, template_name='employees/employee_form.html'):
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('employees:employee-list')
    return render(request, template_name, {'form': form, 'title': 'Edit Employee'})

def employee_delete(request, pk, template_name='employees/employee_confirm_delete.html'):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employees:employee-list')
    return render(request, template_name, {'object': employee})

