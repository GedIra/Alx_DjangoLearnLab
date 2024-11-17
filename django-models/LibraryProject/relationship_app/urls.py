from django.urls import path
from . import views
from .views import list_books, Logout
from .views import LibraryDetailView
from django.contrib.auth.views import LoginView


urlpatterns = [
    path("books/", list_books, name ='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name="relationship_app/login.html"), name='login'),
    path('logout/', Logout, name='logout'),
    path('Admin/', views.admin_view, name='admins_only'),
    path('Member/', views.member_view, name='members_only'),
    path('Librarian/', views.librarian_view, name='librarians_only'),
    path('deleted/', views.DeleteBookView, name='deleted'),
    path('created/', views.CreateBookView, name='created'),
    path('updated/', views.UpdateBookView, name='Updated'),
]
