from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsOwnerOrReadOnlyPermission
from .models import Post, Comment

# Create your views here.

class PostsViewset(viewsets.ModelViewSet):
  serializer_class = PostSerializer
  queryset = Post.objects.all()
  permission_classes = [IsOwnerOrReadOnlyPermission]
  authentication_classes = [JWTAuthentication]
  
  def perform_create(self, serializer):
    serializer.save(author=self.request.user)
    return super().perform_create(serializer)
  
class CommentSViewset(viewsets.ModelViewSet):
  serializer_class = CommentSerializer
  permission_classes = [IsOwnerOrReadOnlyPermission]
  authentication_classes = [JWTAuthentication]
  queryset = Comment.objects.all()
  
  def perform_create(self, serializer):
    serializer.save(author= self.request.user)
    return super().perform_create(serializer)
  