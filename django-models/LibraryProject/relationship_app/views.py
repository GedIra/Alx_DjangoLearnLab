from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .models import Author, Book, Librarian, UserProfile
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import permission_required
from django.views import View

# Create your views here.

def list_books(request):

  books = Book.objects.all()

  context = {'books' : books}

  return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
  model = Library
  template_name = 'relationship_app/library_detail.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      library = self.get_object()
      context['books'] = library.books.all()
      return context
  
def register(request):

  if request.method == 'POST':
    form = UserCreationForm(request.POST)

    if form.is_valid():
      form.save()
      return redirect(reverse('login'))
    
    else:
      form.add_error(None, 'Invalid username or password')
    
  else:
    form = UserCreationForm()

  context = {'form': form}

  return render(request, 'relationship_app/register.html', context)

def has_role(user, role):
  return UserProfile.objects.filter(user=user, role=role).exists()

def Admin(user):
  return has_role(user, 'Admin')

def Member(user):
  return  has_role(user, 'Member')

def Librarian(user):
  return has_role(user, 'Librarian')

@user_passes_test(Admin, login_url='/login/')
def AdminView(request):
  user = request.user
  return render(request, 'relationship_app/admin_view.html', {"user": user})

@user_passes_test(Librarian, login_url='/login/')
def Librarian_view(request):
  libraries = Library.objects.all()
  return render(request, 'relationship_app/librarian_view.html', {"libraries": libraries })

@user_passes_test(Member, login_url='/login/')
def Member_view(request):
  books = Book.objects.all()
  return render(request, 'relationship_app/member_view.html', {'books': books})


# def Logout(request):
#     logout(request)
#     return render(request, 'relationship_app/logout.html')

@login_required(login_url="/login/")
@permission_required("relationship_app.can_delete_book", raise_exception=True)
def DeleteBookView(request):
  try:
    book = Book.objects.get(title='Alvin and the Chipmunks')
  except:
    pass
  else:
    book.delete()
  books = Book.objects.all()
  context = {'books' : books}
  return render(request, 'relationship_app/list_books.html', context)

@login_required(login_url="/login/")
@permission_required("relationship_app.can_add_book", raise_exception=True)
def CreateBookView(request):
  try:
    author = Author.objects.get(name='Ruth Chew')
    book = Book(title='Magic of the Black Mirror', author=author)
  except:
    pass
  else:
    book.save()
  books = Book.objects.all()
  context = {'books' : books}
  return render(request, 'relationship_app/list_books.html', context)

@login_required(login_url="/login/")
@permission_required("relationship_app.can_change_book", raise_exception=True)
def UpdateBookView(request):
  try:
    book = Book.objects.get(title='White Star')
    book.title = 'White Star: A Dog on the Titanic'
  except:
    pass
  else:
    book.save()
  books = Book.objects.all()
  context = {'books' : books}
  return render(request, 'relationship_app/list_books.html', context)




  




