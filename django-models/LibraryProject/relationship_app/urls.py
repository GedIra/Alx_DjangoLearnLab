from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from .views import RegisterView
from .views import LoginView
from .views import LogoutView


urlpatterns = [
    path("books/", list_books, name ='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='LibraryDetailView'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    #path('library/<int:pk>/', ListLibraryBooks.as_view(), name='library_books_list'),

]