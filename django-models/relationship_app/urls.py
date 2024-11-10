from django.urls import path
from .views import listbooks
from .views import ListLibraryBooks


urlpatterns = [
    path("books/", listbooks, name ='listbooks'),
    path('library/', ListLibraryBooks.as_view(), name='library_books_list')

]
