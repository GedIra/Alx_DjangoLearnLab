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
from rest_framework import generics, response
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class UserCreationAPIView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class UserListAPIView(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [IsAuthenticated]
  
  def get(self, request, format=None):
    usernames = [user.id for user in User.objects.all()]
  
    return response.Response(usernames)
    
  
class UserRegisterAPIView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = RegisterSerializer
  
class UserProfileManagementAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [IsAuthenticated]
  
  def get_queryset(self):
    user = self.request.user
    queryset = User.objects.filter(username = user.username)
    return queryset
  

    
    
      
  

  