from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from .views import RegisterView
from .views import LoginView



urlpatterns = [
    path("books/", list_books, name ='list_books'),
    path('library/', LibraryDetailView.as_view(), name='LibraryDetailView'),
    path('register/', RegisterView.as_view(), name='RegisterView'),
    path('login/', LoginView.as_view(), name='login'),

]
