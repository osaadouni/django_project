from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator 

from activities.models import Activity 
from activities.forms import ActivityForm


class ActivityList(ListView):
    model = Activity
    ordering = ['-pk']
    paginate_by = 5
    template_name = 'activities/activity_list.html'
    context_object_name = 'activity_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        activity_list = Activity.objects.order_by('-pk')
        page = self.request.GET.get('page')
        paginator = Paginator(activity_list, self.paginate_by)
        activities = paginator.get_page('page')
        context['object_list'] = activities
        return context


class ActivityDetail(DetailView):
    model = Activity
    template_name = 'activities/activity_detail.html'


class ActivityCreate(CreateView):
    model = Activity
    form_class = ActivityForm
    template_name = 'activities/activity_create_form.html'
    success_url = reverse_lazy('activities:activity-list')

class ActivityUpdate(UpdateView): 
    model = Activity
    form_class = ActivityForm
    template_name = 'activities/activity_edit_form.html'
    success_url = reverse_lazy('activities:activity-list')


class ActivityDelete(DeleteView):
    model = Activity
    success_url = reverse_lazy('activities:activity-list')
    
