from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# Create your models here.


class CustomUserManager(BaseUserManager):
  
  def create_user(self, username_field, email, password=None):
    
    if not email:
      raise ValueError("The email is required")
    
    user = self.model(username=username_field, email=self.normalize_email(email))
    
    user.set_password(password)
    user.save(using = self._db)
    
    return user
  
  def create_superuser(self, username_field, email, password=None):
    
    user = self.create_user(username_field, email=email, password=password)
    
    user.is_admin = True
    user.is_superuser = True
    user.is_staff = True
    user.save(using=self._db)
    
    return user

class User(AbstractUser):

  email = models.EmailField(verbose_name="email address", unique=True, max_length=255)
  
  REQUIRED_FIELDS = ['email']
  
  objects = CustomUserManager
  
  def __str__(self) -> str:
    return self.username
  
User = get_user_model()
  
class Post(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField()
  published_date = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE, null=False)
  

class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=False)
  picture = models.URLField(verbose_name='profile picture', blank=True, null=True)
  dob = models.DateField(verbose_name='date of birth', blank=True, null=True)
  bio = models.TextField(verbose_name='biography', blank=True, null=True)

  
  
