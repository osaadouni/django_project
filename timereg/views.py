from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from timereg.models import TimeReg 
from timereg.forms import TimeRegForm


class UserTestMixin(UserPassesTestMixin):
    def test_func(self):
        return True # self.request.user.username.startswith('omar')


#class TimeRegList(LoginRequiredMixin, UserPassesTestMixin, ListView):
class TimeRegList(LoginRequiredMixin, UserTestMixin, ListView):
    model = TimeReg
    ordering = ['-pk']
    paginate_by = 5
    template_name = 'timereg/timereg_list.html'
    context_object_name = 'timereg_list'

    raise_exception = True
    permission_denied_message = 'Permission denied ! . Go away!!'

    def get_permission_denied_message(self):
        return 'Go away!!!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        timereg_list = TimeReg.objects.order_by('-pk')
        page = self.request.GET.get('page')
        paginator = Paginator(timereg_list, self.paginate_by)
        timereg = paginator.get_page('page')
        context['object_list'] = timereg
        return context

    def render_to_response(self, context):
        rendered = render_to_string(self.template_name, context, self.request)
        return JsonResponse({'data': rendered})


class TimeRegDetail(LoginRequiredMixin, DetailView):
    model = TimeReg
    template_name = 'timereg/timereg_detail.html'

    def render_to_response(self, context):
        rendered = render_to_string(self.template_name, context, self.request)
        return JsonResponse({'data': rendered})


class TimeRegCreate(LoginRequiredMixin, CreateView):
    model = TimeReg
    form_class = TimeRegForm
    template_name = 'timereg/timereg_create_form.html'
    success_url = reverse_lazy('timereg:timereg-list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def my_form_valid(self, form):
        print('TimeRegCreate::form_valid()...')
        self.object = form.save(commit=False)
        hour = form.cleaned_data.get("hour")
        minute = form.cleaned_data.get("minute")
        sec = form.cleaned_data.get("sec")
        time = "{}:{}:{}".format(hour, minute, sec)
        print('TimeRegCreate::form_valid(): time: ', time)

        self.object.time = time
        self.object.created_by = self.request.user 
        self.object.save()
        return super().form_valid(form);

    def render_to_response(self, context):
        rendered = render_to_string(self.template_name, context, self.request)
        return JsonResponse({'data': rendered})


class TimeRegUpdate(LoginRequiredMixin, UpdateView):
    model = TimeReg
    form_class = TimeRegForm
    template_name = 'timereg/timereg_edit_form.html'
    success_url = reverse_lazy('timereg:timereg-list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        time = self.get_object().time
        print('get_initial(): time = ', time )
        initial['hour'], initial['minute'], initial['sec'] = time.split(':')
        return initial

    def render_to_response(self, context):
        rendered = render_to_string(self.template_name, context, self.request)
        return JsonResponse({'data': rendered})


class TimeRegDelete(LoginRequiredMixin, DeleteView):
    model = TimeReg
    success_url = reverse_lazy('timereg:timereg-list')
    template_name = 'timereg/timereg_confirm_delete.html'

    def render_to_response(self, context):
        rendered = render_to_string(self.template_name, context, self.request)
        return JsonResponse({'data': rendered})
