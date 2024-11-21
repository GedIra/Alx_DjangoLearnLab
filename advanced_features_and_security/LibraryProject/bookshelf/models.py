from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
  def create_user(self, username, date_of_birth, password=None):
    if not date_of_birth:
      raise ValueError("Users date of birth is required")

    user = self.model(
        username=username,
        date_of_birth=date_of_birth,
    )
    user.set_password(password)
    user.save(using=self._db)
    return user
  
  def create_superuser(self, username, date_of_birth, password=None):
    user = self.create_user(username, date_of_birth=date_of_birth,password=password)
    
    user.is_staff = True
    user.is_superuser = True
    user.save(using=self._db)
    return user
  
  
class CustomUser(AbstractUser):
  date_of_birth = models.DateField()
  profile_photo = models.ImageField(upload_to=None, null=True, blank=True)
  
  objects = UserManager()
  
  REQUIRED_FIELDS = ['date_of_birth']

###########################

# Create your models here.

class Book(models.Model):
  title = models.CharField(max_length =200)
  author = models.CharField(max_length=100)
  publication_year = models.IntegerField(null = True)

  def __str__(self):
    return f"{self.title} by {self.author}"

