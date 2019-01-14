from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 
from django.core.paginator import Paginator

from .models import Department
from .forms import DepartmentForm


class DepartmentList(ListView):
    model = Department
    ordering = ('-pk',)
    paginate_by = 5
    template_name = 'departments/department_list.html'
    context_object_name = 'department_list'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        department_list = Department.objects.order_by('-pk')
        paginator = Paginator(department_list, self.paginate_by)
        page = self.request.GET.get('page')
        departments = paginator.get_page(page)
        context['object_list'] = departments
        return context


class DepartmentView(DetailView):
    model = Department


class DepartmentCreate(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'departments/department_create_form.html'
    success_url = reverse_lazy('departments:department-list')



class DepartmentUpdate(UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'departments/department_edit_form.html'
    success_url = reverse_lazy('departments:department-list')

class DepartmentDelete(DeleteView):
    model = Department 
    success_url = reverse_lazy('departments:department-list')
