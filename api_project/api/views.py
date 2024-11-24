from django.shortcuts import render
from .serializers import BookSerializer
from .models import Book
from rest_framework import generics
from rest_framework import viewsets

# Create your views here.

class BookList(generics.ListAPIView):
  serializer_class = BookSerializer
  queryset = Book.objects.all()
  
class BookViewSet(viewsets.ModelViewSet):
  serializer_class = BookSerializer
  queryset = Book.objects.all()

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):

  def post(self, request, *args, **kwargs ):
    serializer = self.serializer_class(data=request.data , context={'request': request})
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token, created = Token.objects.get_or_create(user=user)
    
    return Response ({
      'user_id': user.pk,
      'username': user.username,
      'token': token.key 
    })
 
from rest_framework import permissions