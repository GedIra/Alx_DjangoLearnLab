from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import CreateView
from .models import Book
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import permission_required, login_required
from .forms import ExampleForm
from .forms import BookForm, User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
#from django.contrib.auth.mixins import PermissionRequiredMixin

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

def Logout(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

#Create your views here.
# class Create_View(PermissionRequiredMixin, CreateView):
#   model = Book
#   template_name = "bookshelf/create_book.html"
#   fields = ['title', 'author', 'publication_year']
#   permission_required = "bookshelf.can_create"
#   success_url = reverse_lazy('createView')

@permission_required('bookshelf.can_create', raise_exception=True)
def CreateBookView(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('createView')  # Adjust 'book_list' to your desired URL pattern
    else:
        form = BookForm()
    return render(request, 'bookshelf/create_book.html', {'form': form})
  
def BookDetailView(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'bookshelf/book_detail.html', {'book': book}) 
    
@permission_required('bookshelf.can_edit', '/login/')
def EditBookView(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=book.id)  # Redirect to a detail view of the book
    else:
        form = BookForm(instance=book)
    
    return render(request, 'bookshelf/edit_book.html', {'form': form, 'book': book})
  
def BooklistView(request):
    books = Book.objects.all()
    context = {'books' : books}
    return render(request, 'bookshelf/book_list.html', context)

@login_required(login_url="/login/")
def UserProfileUpdateView(request):
    user = User.objects.get(username=request.user.username)
    
    if request.method =='POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userupdate')
    else:
        form = ExampleForm(instance=request.user)
    return render(request, 'bookshelf/form_example.html', {'form': form})
