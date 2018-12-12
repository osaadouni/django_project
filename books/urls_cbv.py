from django.urls import path

from . import views

app_name = 'books'
urlpatterns = [
    path('', views.BookList.as_view(), name='book-list'),
    path('view/<int:pk>', views.BookView.as_view(), name='book-view'),
    path('add', views.BookCreate.as_view(), name='book-add'),
    path('edit/<int:pk>', views.BookUpdate.as_view(), name='book-edit'),
    path('delete/<int:pk>', views.BookDelete.as_view(), name='book-delete'),
]
