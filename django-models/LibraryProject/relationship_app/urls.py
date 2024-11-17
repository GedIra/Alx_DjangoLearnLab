from django.urls import path
from . import views
from .views import list_books
from .views import LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("books/", list_books, name ='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name="relationship_app/login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin_view/', views.AdminView, name='admins_only'),
    path('Member/', views.Member_view, name='members_only'),
    path('Librarian/', views.Librarian_view, name='librarians_only'),
    path('delete_book/', views.DeleteBookView, name='delete_book'),
    path('add_book/', views.CreateBookView, name='add_book'),
    path('edit_book/', views.UpdateBookView, name='edit_book'),
]
