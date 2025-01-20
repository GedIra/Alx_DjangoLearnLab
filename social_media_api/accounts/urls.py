from django.urls import path
from .views import (Register, welcome, Logout,
        UserCreationAPIView, UserListAPIView, UserRegisterAPIView, UserProfileManagementAPIView,
        CustomTokenObtainView
      )

from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

urlpatterns = [
  path('register/',Register.as_view(), name='register'),
  path('check/', welcome, name='check'),
  path('login/', auth_views.LoginView.as_view(), name='login'),
  path('logout/', Logout, name='logout'),
  path('api/users/',UserListAPIView.as_view(), name = "users"),
  path('api/user/create/', UserCreationAPIView.as_view(), name='create_user'),
  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('api/login/', CustomTokenObtainView.as_view(), name='token_obtain'),
  path('api/register/', UserRegisterAPIView.as_view(), name='api_register'),
  path('api/me/<int:pk>/', UserProfileManagementAPIView.as_view(), name='user-detail'),
]
