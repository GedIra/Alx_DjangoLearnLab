from rest_framework import generics
from .models import Book,Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# Create your views here.

class AuthorsAPIView(generics.ListCreateAPIView):
  serializer_class = AuthorSerializer
  def get_queryset(self):
      queryset = Author.objects.all()
      return queryset  

class ListView(generics.ListAPIView):
  permission_classes = [IsAuthenticatedOrReadOnly]
  serializer_class = BookSerializer
  queryset = Book.objects.all()
  
class DetailView(generics.RetrieveAPIView):
  permission_classes = [IsAuthenticatedOrReadOnly]
  serializer_class = BookSerializer
  queryset = Book.objects.all()
  
class CreateView(generics.CreateAPIView):
  permission_classes = [IsAuthenticated]
  serializer_class = BookSerializer
  queryset = Book.objects.all()
  
class UpdateView(generics.UpdateAPIView):
  permission_classes = [IsAuthenticated]
  serializer_class = BookSerializer
  queryset = Book.objects.all()
  
class DeleteView(generics.DestroyAPIView):
  permission_classes = [IsAuthenticated]
  serializer_class = BookSerializer
  queryset = Book.objects.all()
  

  