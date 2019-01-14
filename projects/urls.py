from django.urls import path

from . import views

app_name = 'projects'
urlpatterns = [
    path('', views.ProjectList.as_view(), name='project-list'),
    path('view/<int:pk>', views.ProjectView.as_view(), name='project-view'),
    path('add', views.ProjectCreate.as_view(), name='project-add'),
    path('edit/<int:pk>', views.ProjectUpdate.as_view(), name='project-edit'),
    path('delete/<int:pk>', views.ProjectDelete.as_view(), name='project-delete'),

    path('state', views.ProjectStateList.as_view(), name='state-list'),
    path('state/add', views.ProjectStateCreate.as_view(), name='state-add'),
    path('state/edit/<int:pk>', views.ProjectStateUpdate.as_view(), name='state-edit'),
    path('state/delete/<int:pk>', views.ProjectStateDelete.as_view(), name='state-delete'),

    path('phase', views.ProjectPhaseList.as_view(), name='phase-list'),
    path('phase/add', views.ProjectPhaseCreate.as_view(), name='phase-add'),
    path('phase/edit/<int:pk>', views.ProjectPhaseUpdate.as_view(), name='phase-edit'),
    path('phase/delete/<int:pk>', views.ProjectPhaseDelete.as_view(), name='phase-delete'),
]
