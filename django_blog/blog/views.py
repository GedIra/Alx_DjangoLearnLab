from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm, LoginForm, UserProfileForm, PostForm
from django.urls import reverse_lazy
from .models import UserProfile, User, Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


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
  

class ListPostsView(ListView):
  model = Post
  template_name = "blog/listposts.html"
  ordering = ['title', 'published_date', 'author']
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["posts"] = Post.objects.all()
    return context
  
class PostDetailView(DetailView):
  model = Post
  template_name = 'blog/postdetails.html'
  context_object_name = 'post'
  
class PostCreateView(LoginRequiredMixin, CreateView):
  model = Post
  form_class = PostForm
  template_name = 'blog/createpost.html'
  success_url = reverse_lazy('posts')
  
  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Post
  form_class = PostForm
  template_name = 'blog/createpost.html'
  
  def test_func(self):
    post = self.get_object()
    return (self.request.user == post.author)
  
  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
  
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = Post
  template_name = 'blog/deletepost.html'
  success_url = reverse_lazy('posts')
  
  def test_func(self):
    post = self.get_object()
    return (self.request.user == post.author )
  

  

  

  
  
  
  
  
  