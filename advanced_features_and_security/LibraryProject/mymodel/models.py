from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

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
  
  def create_super_user(self, username, date_of_birth, password=None):
    user = self.create_user(
            username,
            date_of_birth=date_of_birth,
            password=password,
        )
    user.is_staff = True
    user.is_superuser = True
    user.save(using=self._db)
    return user


class CustomUser(AbstractUser):
  date_of_birth = models.DateField()
  profile_photo = models.models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)

  objects = UserManager()

  #USERNAME_FIELD = ""
  REQUIRED_FIELDS = ["date_of_birth"]

  def __str__(self):
      return self.username





# Create your models here.
