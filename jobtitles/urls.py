from django.urls import path

from . import views

app_name = 'jobtitles'
urlpatterns = [
    path('', views.JobTitleList.as_view(), name='jobtitle-list'),
    path('view/<int:pk>', views.JobTitleView.as_view(), name='jobtitle-view'),
    path('add', views.JobTitleCreate.as_view(), name='jobtitle-add'),
    path('edit/<int:pk>', views.JobTitleUpdate.as_view(), name='jobtitle-edit'),
    path('delete/<int:pk>', views.JobTitleDelete.as_view(), name='jobtitle-delete'),
]
