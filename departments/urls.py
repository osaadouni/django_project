from django.urls import path

from . import views

app_name = 'departments'
urlpatterns = [
    path('', views.DepartmentList.as_view(), name='department-list'),
    path('view/<int:pk>', views.DepartmentView.as_view(), name='department-view'),
    path('add', views.DepartmentCreate.as_view(), name='department-add'),
    path('edit/<int:pk>', views.DepartmentUpdate.as_view(), name='department-edit'),
    path('delete/<int:pk>', views.DepartmentDelete.as_view(), name='department-delete'),
]
