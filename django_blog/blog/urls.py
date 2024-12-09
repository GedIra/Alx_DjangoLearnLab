from django.urls import path
from .views import (
  RegisterView, UserProfileUpdateView, UserProfileView,PostDeleteView,
  ListPostsView, PostDetailView, PostCreateView, PostEditView
  )
from . import views

urlpatterns = [
  path('login/', views.LoginView, name='login'),
  path('register/', RegisterView.as_view(), name='register'),
  path('welcome/', views.welcomeView, name='welcome'),
  path('logout/', views.LogoutView, name='logout'),
  path('profile/',UserProfileView.as_view(), name='user_profile'),
  path('profile/update/', UserProfileUpdateView.as_view(), name='profile_update'),
  path('posts/', ListPostsView.as_view(), name='posts'),
  path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
  path('post/new/', PostCreateView.as_view(), name='post_create'),
  path('post/<int:pk>/update/', PostEditView.as_view(), name='post_edit'),
  path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]