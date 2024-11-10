from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .models import Author, Book,Librarian
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

# Create your views here.

def list_books(request):

  books = Book.objects.all()

  context = {'books' : books}

  return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(ListView):

  books = Library.objects.all()

  context = {'books' : books}
  model = Library
  template_name = 'relationship_app/library_detail.html'
  
class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

class LoginView(LoginView):
  template_name = 'relationship_app/login.html'



