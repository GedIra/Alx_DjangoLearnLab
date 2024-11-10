from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Author, Book, Library, Librarian

# Create your views here.

def listbooks(request):

  books = Book.objects.all()

  context = {'books' : books}

  return render(request, 'relationship_app/list_books.html', context)

class ListLibraryBooks(ListView):
  model = Library
  template_name = 'relationship_app/library_detail.html'





