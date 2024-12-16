from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import CreateView
from .models import Book
from django.urls import reverse_lazy
from django.contrib.auth.decorators import permission_required
from .forms import BookForm
#from django.contrib.auth.mixins import PermissionRequiredMixin


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
def EditBookView(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=book.id)  # Redirect to a detail view of the book
    else:
        form = BookForm(instance=book)
    
    return render(request, 'bookshelf/edit_book.html', {'form': form, 'book': book})
  
