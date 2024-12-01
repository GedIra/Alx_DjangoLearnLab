from django.urls import path, include
from . import views

urlpatterns = [
  path('authors/', views.AuthorsAPIView.as_view(),name='authors'),
  path('books/', views.ListView.as_view(), name='list_books'),
  path('books/<int:pk>/', views.DetailView.as_view(), name='book_detail'),
  path('create/', views.CreateView.as_view(), name='book_create'),
  path('update/<int:pk>/', views.UpdateView.as_view(), name='book_update'),
  path('delete/<int:pk>/', views.DeleteView.as_view(), name='book_delete')

]
