from django.db import models

# Create your models here.
class Book(models.Model):
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=50)
  publication_year = models.IntegerField(null=True)
  
  def __str__(self):
    return f'{self.title} by {self.author}'

