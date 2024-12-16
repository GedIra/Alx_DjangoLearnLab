from django.urls import path
from .views import Register, welcome
from django.contrib.auth import views as auth_views


urlpatterns = [
  path('register/',Register.as_view(), name='register'),
  path('check/', welcome, name='check'),
  path("login/", auth_views.LoginView.as_view()),
]
