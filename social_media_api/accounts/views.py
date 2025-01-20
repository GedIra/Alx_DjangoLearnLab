from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.urls import reverse_lazy
from .models import User
from .forms import UserCreationForm

# Create your views here.

class Register(generic.CreateView):
  model = User
  form_class = UserCreationForm
  template_name = 'accounts/register.html'
  success_url = reverse_lazy('check')
  

def welcome(request):
  return render(request, 'accounts/welcome.html')

def Logout(request):
  logout(request)
  return render(request, 'accounts/logout.html')



### APIVIEWS
from rest_framework import generics
from rest_framework.response import Response
#from .serializers import PostSerializer, CommentSerializer
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
#from .models import Post, Comment


class UserCreationAPIView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class UserListAPIView(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [IsAuthenticated]
  authentication_classes = [TokenAuthentication]
  
  def get(self, request, format=None):
    usernames = [user.username for user in User.objects.all()]
  
    return Response(usernames)
    
  
class UserRegisterAPIView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = RegisterSerializer
  
class UserProfileManagementAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]
  
  def get_queryset(self):
    user = self.request.user
    queryset = User.objects.filter(username = user.username)
    return queryset

class CustomTokenObtainView(ObtainAuthToken):
  def post(self, request, *args, **kwargs):
    serializer = self.serializer_class(data=request.data, context={"request": request})
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token, created = Token.objects.get_or_create(user=user)
    
    return Response({
      'user': user.username,
      'token': token.key 
    })
    
# class PostlistCreateAPIView(generics.ListCreateAPIView):
#   serializer_class = PostSerializer
#   queryset = Post.objects.all()
#   permission_classes = [IsAuthenticatedOrReadOnly]
#   authentication_classes = [TokenAuthentication]
  
#   def perform_create(self, serializer):
#     serializer.save(author=self.request.user)
#     return super().perform_create(serializer)
  
# class PostRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
#   serializer_class = PostSerializer
#   permission_classes = [IsAuthenticatedOrReadOnly]
#   authentication_classes = [TokenAuthentication]
  
#   def get_queryset(self):
#     user = self.request.user
#     if user.is_authenticated:
#       return Post.objects.filter(author=user)
#     return Post.objects.all()
  
# class CommentListCreateapiView(generics.ListCreateAPIView):
#   serializer_class = CommentSerializer
#   permission_classes = [IsAuthenticatedOrReadOnly]
#   authentication_classes = [TokenAuthentication]
#   queryset = Comment.objects.all()
  
#   def perform_create(self, serializer):
#     serializer.save(author= self.request.user)
#     return super().perform_create(serializer)
  
  
# class CommentRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
#   serializer_class = CommentSerializer
#   permission_classes = [IsAuthenticatedOrReadOnly]
#   authentication_classes = [TokenAuthentication]
  
#   def get_queryset(self):
#     user = self.request.user
#     if user.is_authenticated:
#       return Comment.objects.filter(author=user)
#     return Comment.objects.all()
  

  