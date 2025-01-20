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
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken


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
    
  

  