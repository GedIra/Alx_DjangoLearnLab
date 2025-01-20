from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth import get_user_model

# Create your models here.

class CustomUserManager(BaseUserManager):
  def create_user(self, username, email, password= None):
    if not email:
      raise ValueError("The email is required")
    
    user = self.model(username=username, email=self.normalize_email(email))
    
    user.set_password(password)
    user.save(using = self._db)
    return user

  def create_superuser(self, username, email, password=None):
    user = self.create_user(username, email=email, password=password)
    user.is_admin = True
    user.is_staff = True
    user.is_superuser = True
    user.save(using=self._db)
    return user

class User(AbstractUser):
  email = models.EmailField(verbose_name="email address", unique=True, max_length=255)
  followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
  bio = models.TextField(blank=True, null=True)
  profile_picture = models.ImageField(null=True, blank=True)
  REQUIRED_FIELDS = ['email']
  objects = CustomUserManager()
  
  def __str__(self):
    return self.username
  
User = get_user_model()
  
  
