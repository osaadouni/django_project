from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from books.models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'pages']


def book_list(request, template_name='books/book_list.html'):
    #books = Book.objects.all()
    books = Book.objects.order_by('-pk')
    context = {}
    context['object_list'] = books
    return render(request, template_name, context)

def book_view(request, pk, template_name='books/book_detail.html'):
    book = get_object_or_404(Book, pk=pk)
    context = { 'object': book }
    return render(request, template_name, context)


def book_create(request, template_name='books/book_form.html'):
    form = BookForm(request.POST or None)
    if form.is_valid(): 
        form.save()
        return redirect('books:book-list')
    return render(request, template_name, {'form': form, 'title': 'Add Book'})


def book_update(request, pk, template_name='books/book_form.html'):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('books:book-list')
    return render(request, template_name, {'form': form, 'title': 'Edit Book'})


def book_delete(request, pk, template_name='books/book_confirm_delete.html'):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('books:book-list')
    return render(request, template_name, {'object': book})

  
