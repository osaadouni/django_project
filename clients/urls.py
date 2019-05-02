from django.urls import path

from . import views

app_name = 'clients'
urlpatterns = [
    path('', views.ClientList.as_view(), name='client-list'),
    path('view/<int:pk>', views.ClientDetail.as_view(), name='client-detail'),
    path('add', views.ClientCreate.as_view(), name='client-add'),
    path('edit/<int:pk>', views.ClientUpdate.as_view(), name='client-edit'),
    path('delete/<int:pk>', views.ClientDelete.as_view(), name='client-delete'),
    #path('search/', views.ClientSearch.as_view(), name='client-search'),
]
