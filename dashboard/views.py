from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

@method_decorator(login_required, name='dispatch')
class DashboardView(View):
    
    def get(self, request, *args, **kwargs):
        #return HttpResponse('Welcome home!')
        return render(request, 'dashboard/home.html', {})

