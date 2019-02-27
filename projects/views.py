from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.template.loader import render_to_string


from projects.models import Project, ProjectState, ProjectPhase
from .forms import ProjectForm, ProjectStateForm, ProjectPhaseForm


class ProjectList(ListView):
    model = Project
    ordering = ['-pk']
    paginate_by = 5
    template_name = 'projects/project_list.html'
    context_object_name = 'project_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_list = Project.objects.order_by('-pk')
        paginator = Paginator(project_list, self.paginate_by)
         
        page = self.request.GET.get('page')
       
        projects = paginator.get_page(page)
 
        context['object_list'] = projects
        return context

    def render_to_response(self, context):
        template = self.template_name
        rendered = render_to_string(template, context, self.request)
        return JsonResponse({'data': rendered})



class ProjectView(DetailView):
    model = Project


class ProjectCreate(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_create_form.html'
    success_url = reverse_lazy('projects:project-list')

    def render_to_response(self, context):
        rendered = render_to_string(self.template_name, context, self.request)
        return JsonResponse({'data': rendered})


class ProjectUpdate(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_edit_form.html'
    success_url = reverse_lazy('projects:project-list')


class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('projects:project-list')
             


"""
Project States Classes
"""
class ProjectStateList(ListView):
    model = ProjectState
    ordering = ['-pk']
    paginate_by = 5
    template_name = 'projects/state/state_list.html'
    context_object_name = 'state_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        state_list = ProjectState.objects.order_by('-pk')
        paginator = Paginator(state_list, self.paginate_by)
         
        page = self.request.GET.get('page')
       
        states = paginator.get_page(page)
 
        context['object_list'] = states
        return context

class ProjectStateView(DetailView):
    model = ProjectState


class ProjectStateCreate(CreateView):
    model = ProjectState
    form_class = ProjectStateForm
    template_name = 'projects/state/state_create_form.html'
    success_url = reverse_lazy('projects:state-list')

class ProjectStateUpdate(UpdateView):
    model = ProjectState
    form_class = ProjectStateForm
    template_name = 'projects/state/state_edit_form.html'
    success_url = reverse_lazy('projects:state-list')


class ProjectStateDelete(DeleteView):
    model = ProjectState
    template_name = 'projects/state/state_confirm_delete.html'
    success_url = reverse_lazy('projects:state-list')
             
"""
Project Phase Classes
"""
class ProjectPhaseList(ListView):
    model = ProjectPhase
    ordering = ['-pk']
    paginate_by = 5
    template_name = 'projects/phase/phase_list.html'
    context_object_name = 'phase_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        phase_list = ProjectPhase.objects.order_by('-pk')
        paginator = Paginator(phase_list, self.paginate_by)
         
        page = self.request.GET.get('page')
       
        phases = paginator.get_page(page)
 
        context['object_list'] = phases
        return context

class ProjectPhaseView(DetailView):
    model = ProjectPhase


class ProjectPhaseCreate(CreateView):
    model = ProjectPhase
    form_class = ProjectPhaseForm
    template_name = 'projects/phase/phase_create_form.html'
    success_url = reverse_lazy('projects:phase-list')

class ProjectPhaseUpdate(UpdateView):
    model = ProjectPhase
    form_class = ProjectPhaseForm
    template_name = 'projects/phase/phase_edit_form.html'
    success_url = reverse_lazy('projects:phase-list')


class ProjectPhaseDelete(DeleteView):
    model = ProjectPhase
    template_name = 'projects/phase/phase_confirm_delete.html'
    success_url = reverse_lazy('projects:phase-list')
             
