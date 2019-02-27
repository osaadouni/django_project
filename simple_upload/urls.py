from django.urls import path

from . import views

app_name = 'simple_upload'
urlpatterns = [
    path('', views.simple_upload, name='simple-upload'),
    path('model_form_upload/', views.model_form_upload, name='model-form-upload'),
]
