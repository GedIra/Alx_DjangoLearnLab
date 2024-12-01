from rest_framework import generics
from .models import Book,Author
from .serializers import BookSerializer, AuthorSerializer

# Create your views here.

class AuthorsAPIView(generics.ListCreateAPIView):
  serializer_class = AuthorSerializer
  def get_queryset(self):
      queryset = Author.objects.all()
      return queryset  

class ListView(generics.ListAPIView):
  serializer_class = BookSerializer
  queryset = Book.objects.all()
  
class DetailView(generics.RetrieveAPIView):
  serializer_class = BookSerializer
  queryset = Book.objects.all()
  
class CreateView(generics.CreateAPIView):
  serializer_class = BookSerializer
  queryset = Book.objects.all()
  
class UpdateView(generics.UpdateAPIView):
  serializer_class = BookSerializer
  queryset = Book.objects.all()
  
class DeleteView(generics.DestroyAPIView):
  serializer_class = BookSerializer
  queryset = Book.objects.all()
  

  