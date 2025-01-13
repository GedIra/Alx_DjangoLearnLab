from django.urls import path
from .views import CreateBookView, EditBookView, BookDetailView, BooklistView, register, UserProfileUpdateView, Logout
#from .views import Create_View
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name="bookshelf/login.html"), name='login'),
    path('logout/', Logout, name='logout'),
    path('create/', CreateBookView, name='createView'),
    path('books/', BooklistView, name='books'),
    path('books/<int:book_id>/', BookDetailView, name='book_detail'),
    path('books/<int:book_pk>/edit/', EditBookView, name='edit_book'),
    path('myprofile/', UserProfileUpdateView, name='userupdate'),
    #path('create/', Create_View.as_view(), name='CreateView')
]

