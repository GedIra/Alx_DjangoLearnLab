from django.db import models

# Create your models here.

"""_summary_
Author table/model has only the author's name

Returns:
  _type_: _description_
  string: the Author's name - author objects will be seen by his name in the serializers
"""

class Author(models.Model):
  name = models.CharField(max_length=50, unique=True)
  
  def __str__(self) -> str:
    return self.name

"""_summary_
Book table/model author has a foreign key to the Author table

Returns:
  _type_: _description_
  string: Book objects will be presented as title and it's author's name. e.g: THE SUN by David F. Gorge

""" 
class Book(models.Model):
  title = models.CharField(max_length=50)
  author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
  publication_year = models.IntegerField()
  
  def __str__(self) -> str:
    return f"{self.title} by {self.author}"

