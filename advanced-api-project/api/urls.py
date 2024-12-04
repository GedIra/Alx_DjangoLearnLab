from django.urls import path, include
from . import views

urlpatterns = [
  path('authors/', views.AuthorsAPIView.as_view(),name='author-list'),
  path('books/', views.ListView.as_view(), name='list_books'),
  path('books/<int:pk>/', views.DetailView.as_view(), name='book_detail'),
  path('books/create/', views.CreateView.as_view(), name='book_create'),
  path('books/update/<int:pk>/', views.UpdateView.as_view(), name='book_update'),
  path('books/delete/<int:pk>/', views.DeleteView.as_view(), name='book_delete')

]
