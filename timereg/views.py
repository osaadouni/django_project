from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.template.loader import render_to_string


from .models import TimeReg
from .forms import TimeRegForm
from clients.models import Client


class TimeRegList(ListView):
    #model = TimeReg
    ordering = ['-pk']
    paginate_by = 5
    template_name = 'timereg/timereg_list.html'
    context_object_name = 'timereg_list'

 
    def get_queryset(self):
        client_id = self.kwargs.get('client_id', None)
        if client_id: 
            self.client = get_object_or_404(Client, pk=client_id)
            return TimeReg.objects.filter(client=self.client).order_by('-pk')
        else: 
            return TimeReg.objects.order_by('-pk')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # timereg_list = TimeReg.objects.order_by('-pk')
        timereg_list = self.get_queryset() 
        paginator = Paginator(timereg_list, self.paginate_by)
        page = self.request.GET.get('page')
        timereg = paginator.get_page(page)
        context['object_list'] = timereg
        context['client_list'] = Client.objects.order_by('name')

        client_id = self.kwargs.get('client_id', None)
        if client_id: 
            context['client_id'] = client_id

        return context

    def render_to_response(self, context):
        template = self.template_name
        rendered = render_to_string(template, context, self.request)
        return JsonResponse({'data': rendered})



class TimeRegDetail(DetailView):
    model = TimeReg
    template_name = 'timereg/timereg_detail.html'

    def render_to_response(self, context):
        rendered = render_to_string(self.template_name, context, self.request)
        return JsonResponse({'data': rendered})


class TimeRegCreate(CreateView):
    model = TimeReg
    form_class = TimeRegForm
    template_name = 'timereg/timereg_create_form.html'
    success_url = reverse_lazy('timereg:timereg-list')

    def render_to_response(self, context):
        rendered = render_to_string(self.template_name, context, self.request)
        return JsonResponse({'data': rendered})


class TimeRegUpdate(UpdateView):
    model = TimeReg
    form_class = TimeRegForm
    template_name = 'timereg/timereg_edit_form.html'
    success_url = reverse_lazy('timereg:timereg-list')

    def render_to_response(self, context):
        rendered = render_to_string(self.template_name, context, self.request)
        return JsonResponse({'data': rendered})

class TimeRegDelete(DeleteView):
    model = TimeReg
    success_url = reverse_lazy('timereg:timereg-list')
    template_name = 'timereg/timereg_confirm_delete.html'
             
    def render_to_response(self, context):
        rendered = render_to_string(self.template_name, context, self.request)
        return JsonResponse({'data': rendered})


