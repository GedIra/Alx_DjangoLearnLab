from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
  name = models.CharField(max_length = 50)

  def __str__(self):
    return self.name

class Book(models.Model):
  title = models.CharField(max_length = 50)
  author = models.ForeignKey(Author, on_delete = models.CASCADE, related_name = "books")

  class Meta:
    permissions = [
      ("can_add_book", "can add a new book"),
      ("can_change_book", "can edit the existing book"),
      ("can_delete_book", "can delete any book")
    ]

  def __str__(self):
    return self.title

class Library(models.Model):
  name = models.CharField(max_length = 50)
  books = models.ManyToManyField(Book, related_name = 'library')

  def __str__(self):
    return self.name

class Librarian(models.Model):
  name = models.CharField(max_length = 50)
  library = models.OneToOneField(Library, on_delete = models.CASCADE)

  def __str__(self):
    return self.name

class UserProfile(models.Model):
  class Role(models.TextChoices):
    admin = 'Admin'
    member = 'Member'
    librarian = 'Librarian'
  
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  role = models.CharField(choices=Role, max_length=10, default=Role.member)

  def __str__(self) -> str:
    return f'{self.user.username} - {self.role}'



  

  






