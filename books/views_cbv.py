from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from books.models import Book


class BookList(ListView):
    model = Book
    ordering = ['-pk']
    #paginate_by = 5
    #template_name = 'books/books.html' # to override the default template 


class BookView(DetailView):
    model = Book


class BookCreate(CreateView):
    model = Book
    fields = ['name', 'pages']
    template_name = 'books/book_form_add.html'
    success_url = reverse_lazy('books:book-list')

class BookUpdate(UpdateView):
    model = Book
    fields = ['name', 'pages']
    template_name = 'books/book_form_edit.html'
    success_url = reverse_lazy('books:book-list')
 
class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books:book-list')
