from django.urls import path

from . import views

app_name = 'timereg'
urlpatterns = [
    path('', views.TimeRegList.as_view(), name='timereg-list'), 
    path('view/<int:pk>', views.TimeRegDetail.as_view(), name='timereg-detail'),
    path('add', views.TimeRegCreate.as_view(), name='timereg-add'),
    path('edit/<int:pk>', views.TimeRegUpdate.as_view(), name='timereg-edit'),
    path('delete/<int:pk>', views.TimeRegDelete.as_view(), name='timereg-delete'),
]
