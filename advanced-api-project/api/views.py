from rest_framework import generics
from .models import Book,Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework
from rest_framework import filters

# Create your views here.

class AuthorsAPIView(generics.ListCreateAPIView):
  serializer_class = AuthorSerializer
  def get_queryset(self):
    queryset = Author.objects.all()
    return queryset  

class ListView(generics.ListAPIView):
  permission_classes = [IsAuthenticatedOrReadOnly]
  serializer_class = BookSerializer
  filter_backends = [filters.SearchFilter, filters.OrderingFilter, rest_framework.DjangoFilterBackend]
  search_fields = ['title', 'author__name']
  filterset_fields = ['title', 'author', 'publication_year']
  ordering_fields = ['title', 'publication_year']
  ordering = ['title']
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
  

  