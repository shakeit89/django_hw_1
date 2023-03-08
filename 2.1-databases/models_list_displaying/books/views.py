from django.shortcuts import render
from .models import Book


def books_view(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)

def books_list(request):
    template = 'books/books_list_extend.html'
    books = Book.objects.all()

    context = {'books': books}
    return render(request, template, context)
