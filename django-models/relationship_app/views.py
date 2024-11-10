from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .models import Author, Book, Library, Librarian
from .models import Library

# Create your views here.

def listbooks(request):

  books = Book.objects.all()

  context = {'books' : books}

  return render(request, 'relationship_app/list_books.html', context)

class ListLibraryBooks(ListView):

  books = Library.book.all()

  context = {'books' : books}
  model = Library
  template_name = 'relationship_app/library_detail.html'





