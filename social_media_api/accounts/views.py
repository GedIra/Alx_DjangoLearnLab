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


