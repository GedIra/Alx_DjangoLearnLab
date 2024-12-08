from django.urls import path
from .views import RegisterView, UserProfileUpdateView, UserProfileView
from . import views

urlpatterns = [
  path('login/', views.LoginView, name='login'),
  path('register/', RegisterView.as_view(), name='register'),
  path('welcome/', views.welcomeView, name='welcome'),
  path('logout/', views.LogoutView, name='logout'),
  path('profile/',UserProfileView.as_view(), name='user_profile'),
  path('profile/update/', UserProfileUpdateView.as_view(), name='profile_update'),
  
]