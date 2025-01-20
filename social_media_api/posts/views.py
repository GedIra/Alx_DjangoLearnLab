from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Post, Comment

# Create your views here.

class PostlistCreateAPIView(generics.ListCreateAPIView):
  serializer_class = PostSerializer
  queryset = Post.objects.all()
  permission_classes = [IsAuthenticatedOrReadOnly]
  authentication_classes = [TokenAuthentication]
  
  def perform_create(self, serializer):
    serializer.save(author=self.request.user)
    return super().perform_create(serializer)
  
class PostRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = PostSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]
  authentication_classes = [TokenAuthentication]
  
  def get_queryset(self):
    user = self.request.user
    if user.is_authenticated:
      return Post.objects.filter(author=user)
    return Post.objects.all()
  
class CommentListCreateapiView(generics.ListCreateAPIView):
  serializer_class = CommentSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]
  authentication_classes = [TokenAuthentication]
  queryset = Comment.objects.all()
  
  def perform_create(self, serializer):
    serializer.save(author= self.request.user)
    return super().perform_create(serializer)
  
  
class CommentRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = CommentSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]
  authentication_classes = [TokenAuthentication]
  
  def get_queryset(self):
    user = self.request.user
    if user.is_authenticated:
      return Comment.objects.filter(author=user)
    return Comment.objects.all()