from django.urls import path
from .views import CreateBookView, EditBookView, BookDetailView
#from .views import Create_View


urlpatterns = [
    path('create/', CreateBookView, name='createView'),
    path('books/<int:book_id>/', BookDetailView, name='book_detail'),
    path('books/<int:book_id>/edit/', EditBookView, name='edit_book'),
    #path('create/', Create_View.as_view(), name='CreateView')
]

