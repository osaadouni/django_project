from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from django.urls import reverse_lazy 
from django.utils.decorators import method_decorator 
from django.views.generic import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.contrib.messages.views import SuccessMessageMixin

from .forms import SignUpForm


def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')

    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


class UserCreateView(CreateView):
    form_class = SignUpForm  
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        valid =  super().form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1') 
        new_user = authenticate(username=username, password=password)
        auth_login(self.request, new_user)
        return valid


@method_decorator(login_required, name='dispatch')
class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email', )
    template_name = 'accounts/account_edit.html'
    success_url = reverse_lazy('accounts:account_edit')
    success_message = 'Account was updated successfully!'  


    def get_object(self):
       return self.request.user 




@method_decorator(login_required, name='dispatch')
class UserDetailView(DetailView):
    model = User
    template_name = 'accounts/account_detail.html'
    
    def get_object(self):
       return self.request.user 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
