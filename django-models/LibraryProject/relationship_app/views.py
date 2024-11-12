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
from django.contrib.auth.views import LogoutView
from django.shortcuts import get_object_or_404
from django.contrib.auth import login
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

  def get_queryset(self):
        # Use the primary key from the URL to get the library
        # library_pk = self.kwargs.get('pk')
        # library = get_object_or_404(Library, pk=library_pk)
        # return library.book.all()

        library_1 = Library.objects.get(name="Ikaze Library")
        return library_1.book.all()

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      # Add the library object to the context
      context['library'] = get_object_or_404(Library, pk=self.kwargs.get('pk'))
      return context
  
class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

class LoginView(LoginView):
  template_name = 'relationship_app/login.html'

class LogoutView(LogoutView):
  template_name = 'relationship_app/logout.html'




