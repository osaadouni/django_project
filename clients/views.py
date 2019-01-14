from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator 


from clients.models import Client
from .forms import ClientForm


class ClientList(ListView):
    model = Client  # same as Client.objects.all() 
    #queryset = Client.objects.order_by('-pk')
    ordering = ['-pk']
    paginate_by = 5
    #paginator_class = Paginator 
    template_name = 'clients/client_list.html' # to override the default template 
    context_object_name = "client_list"
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        client_list = Client.objects.order_by('-pk')
        paginator = Paginator(client_list, self.paginate_by)   

        page = self.request.GET.get('page')
        
        clients = paginator.get_page(page)

        context['object_list'] = clients  
        return context  


class ClientView(DetailView):
    model = Client


class ClientCreate(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'clients/client_create_form.html'
    success_url = reverse_lazy('clients:client-list')

class ClientUpdate(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'clients/client_edit_form.html'
    success_url = reverse_lazy('clients:client-list')
 
class ClientDelete(DeleteView):
    model = Client
    success_url = reverse_lazy('clients:client-list')



class AboutView(TemplateView):
    template_name = 'about.html' 
