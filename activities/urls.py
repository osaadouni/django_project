from django.urls import path

from . import views

app_name = 'activities'
urlpatterns = [
    path('', views.ActivityList.as_view(), name='activity-list'), 
    path('view/<int:pk>', views.ActivityDetail.as_view(), name='activity-detail'),
    path('add', views.ActivityCreate.as_view(), name='activity-add'),
    path('edit/<int:pk>', views.ActivityUpdate.as_view(), name='activity-edit'),
    path('delete/<int:pk>', views.ActivityDelete.as_view(), name='activity-delete'),
]
