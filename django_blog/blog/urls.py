from django.urls import path
from .views import (
  RegisterView, UserProfileUpdateView, UserProfileView,PostDeleteView,
  PostsListView, PostDetailView, PostCreateView, PostEditView, PostByTagListView,
  CommentListView, CommentCreateView, CommentUpdateView, CommentDeleteView
  )
from . import views

urlpatterns = [
  path('login/', views.LoginView, name='login'),
  path('register/', RegisterView.as_view(), name='register'),
  path('welcome/', views.welcomeView, name='welcome'),
  path('logout/', views.LogoutView, name='logout'),
  path('profile/',UserProfileView.as_view(), name='user_profile'),
  path('profile/update/', UserProfileUpdateView.as_view(), name='profile_update'),
  path('posts/', PostsListView.as_view(), name='posts'),
  path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
  path('post/new/', PostCreateView.as_view(), name='post_create'),
  path('post/<int:pk>/update/', PostEditView.as_view(), name='post_edit'),
  path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
  path('post/comments/', CommentListView.as_view(), name='comments_list'),
  path('post/comment/<int:pk>/new/', CommentCreateView.as_view(), name='comment_add'),
  path('post/comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_edit'),
  path('post/comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
  path('tags/<str:tag_name>/', PostByTagListView.as_view(), name='post_by_tag'),
]