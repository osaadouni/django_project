from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.db.models import Q

from clients.models import Client
from .forms import ClientForm, ClientSearchForm


class ClientList(ListView):
    model = Client  # same as Client.objects.all() 
    ordering = ['-pk']
    paginate_by = 5
    template_name = 'clients/client_list.html' # to override the default template
    context_object_name = "client_list"
    form_class = ClientSearchForm


    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


    def get_queryset(self):
        print(f'ClientList::get_queryset()')
        form = self.form_class(self.request.POST or None)
        if form.is_valid():
           keyword = form.cleaned_data['keyword']
           return Client.objects.filter(Q(company_name__icontains=keyword) | Q(name__icontains=keyword)).order_by('-pk')
        return Client.objects.order_by('-pk')


    def get_context_data(self, **kwargs):
        print(f'ClientList::get_context_data()')
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        client_list = self.get_queryset() # Client.objects.order_by('-pk')
        paginator = Paginator(client_list, self.paginate_by)   
        page = self.request.GET.get('page')
        clients = paginator.get_page(page)
        context['object_list'] = clients
        context['form'] = self.form_class(self.request.POST or None)
        return context

    def render_to_response(self, context):
        rendered = render_to_string(self.template_name, context, self.request)
        return JsonResponse({'data': rendered})


class ClientDetail(DetailView):
    model = Client
    template_name = 'clients/client_detail.html'

    def render_to_response(self, context):
        rendered = render_to_string(self.template_name, context, self.request)
        return JsonResponse({'data': rendered})


class ClientCreate(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'clients/client_create_form.html'
    success_url = reverse_lazy('clients:client-list')

    def render_to_response(self, context):
        rendered = render_to_string(self.template_name, context, self.request)
        return JsonResponse({'data': rendered})


class ClientUpdate(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'clients/client_edit_form.html'
    success_url = reverse_lazy('clients:client-list')

    def render_to_response(self, context):
        rendered = render_to_string(self.template_name, context, self.request)
        return JsonResponse({'data': rendered})


class ClientDelete(DeleteView):
    model = Client
    success_url = reverse_lazy('clients:client-list')
    template_name = 'clients/client_confirm_delete.html'

    def render_to_response(self, context):
        rendered = render_to_string(self.template_name, context, self.request)
        return JsonResponse({'data': rendered})

