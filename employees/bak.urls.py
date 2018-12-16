from django.urls import path

from . import views

app_name = 'employees'
urlpatterns = [
    path('', views.employee_list, name='employee-list'),
    path('view/<int:pk>', views.employee_view, name='employee-view'),
    path('add', views.employee_create, name='employee-add'),
    path('edit/<int:pk>', views.employee_update, name='employee-edit'),
    path('delete/<int:pk>', views.employee_delete, name='employee-delete'),
]
