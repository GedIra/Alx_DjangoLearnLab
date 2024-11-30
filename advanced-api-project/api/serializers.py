#start by importing all neccessary modules
from rest_framework import serializers
from api.models import Book, Author
import datetime

#Book Model serializer
class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book

    fields = '__all__'
    
  """ 
  1. Custom validation to check if the year is not in the future or negative.
  2. If so raise validation error with a custom message.
  """
  def validate_publication_year(self, value):
    current_year = datetime.datetime.now().year
   
    if value > current_year or value < 1:
      message = 'Invalid book publication year'
      raise serializers.ValidationError(message)
  
    return value
  
#Author model serializers 
    
class AuthorSerializer(serializers.ModelSerializer):
  
  """_summary_
  1. We start by serializing the bokk model.
  2. To serializer a nested relaionship we have to nest serializers within other serializers.
  3. We done this through books. An author can be associated with various books as Book model as a foreign key
      refrencinng authors model. so we can get all books associated to the autho through books in serialization.
  4. Many=True allowing many books to be displayed (as one author can be associated with many books)
  5. read_ony=True, avoid eaditing the data
  """
  books = BookSerializer(many=True, read_only=True)
  
  class Meta:
    model = Author
    fields = ['name', 'books']