from django.urls import path

from . import views

app_name = 'employees'
urlpatterns = [
    path('', views.EmployeeList.as_view(), name='employee-list'),
    path('view/<int:pk>', views.EmployeeView.as_view(), name='employee-view'),
    path('add', views.EmployeeCreate.as_view(), name='employee-add'),
    path('edit/<int:pk>', views.EmployeeUpdate.as_view(), name='employee-edit'),
    path('delete/<int:pk>', views.EmployeeDelete.as_view(), name='employee-delete'),
]
