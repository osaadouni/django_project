from django.urls import path

from . import views

app_name = 'books'
urlpatterns = [
    path('', views.book_list, name='book-list'),
    path('view/<int:pk>', views.book_view, name='book-view'),
    path('add', views.book_create, name='book-add'),
    path('edit/<int:pk>', views.book_update, name='book-edit'),
    path('delete/<int:pk>', views.book_delete, name='book-delete'),
]
