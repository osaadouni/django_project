from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator 


from jobtitles.models import JobTitle
from .forms import JobTitleForm


class JobTitleList(ListView):
    model = JobTitle  # same as JobTitle.objects.all() 
    #queryset = JobTitle.objects.order_by('-pk')
    ordering = ['-pk']
    paginate_by = 5
    #paginator_class = Paginator 
    template_name = 'jobtitles/jobtitle_list.html' # to override the default template 
    context_object_name = "jobtitle_list"
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        jobtitle_list = JobTitle.objects.order_by('-pk')
        paginator = Paginator(jobtitle_list, self.paginate_by)   

        page = self.request.GET.get('page')
        
        jobtitles = paginator.get_page(page)

        context['object_list'] = jobtitles  
        return context  


class JobTitleView(DetailView):
    model = JobTitle


class JobTitleCreate(CreateView):
    model = JobTitle
    form_class = JobTitleForm
    template_name = 'jobtitles/jobtitle_create_form.html'
    success_url = reverse_lazy('jobtitles:jobtitle-list')

class JobTitleUpdate(UpdateView):
    model = JobTitle
    form_class = JobTitleForm
    template_name = 'jobtitles/jobtitle_edit_form.html'
    success_url = reverse_lazy('jobtitles:jobtitle-list')
 
class JobTitleDelete(DeleteView):
    model = JobTitle
    success_url = reverse_lazy('jobtitles:jobtitle-list')



class AboutView(TemplateView):
    template_name = 'about.html' 
