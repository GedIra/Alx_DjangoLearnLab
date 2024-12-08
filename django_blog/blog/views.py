from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth import views, authenticate, login, logout
from .forms import UserCreationForm, LoginForm, UserProfileForm
from django.urls import reverse_lazy
from django.contrib import messages
from .models import UserProfile, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class RegisterView(CreateView):
  model = User
  form_class = UserCreationForm
  template_name = 'blog/register.html'
  success_url = reverse_lazy('login')
  
def welcomeView(request):
  return render(request, 'blog/welcome.html')

def LoginView(request):
  next_url = request.GET.get('next', reverse_lazy('welcome'))  # Get the next URL parameter or use 'welcome' as default
    
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect(next_url)  # Redirect to the next URL
      else:
        form.add_error(None, 'Invalid username or password')
  else:
    form = LoginForm()
    
  return render(request, 'blog/login.html', {'form': form, 'next': next_url})

def LogoutView(request):
  logout(request)
  return render(request, 'blog/logout.html')

class UserProfileView(DetailView):
  model = UserProfile
  template_name = 'blog/profiledetails.html'
  context_object_name = 'profile'
  
  def get_object(self, queryset = None):
    return UserProfile.objects.get(user= self.request.user)
  
#save()

class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
  model = UserProfile
  exclude = ['user']
  form_class = UserProfileForm
  template_name = 'blog/userprofileupdate.html'
  success_url = reverse_lazy('user_profile')
  
  def get_object(self, queryset = None):
    return UserProfile.objects.get(user=self.request.user)
  


  