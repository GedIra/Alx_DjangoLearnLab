from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Author, Book
from django.contrib.auth import get_user_model

class AuthorTest(APITestCase):
  def test_create_author(self):
    url = reverse('author-list')  # Ensure 'author-list' is the name of your URL pattern for the authors endpoint
    data = {'name': 'Ged Ira'}
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Author.objects.count(), 1)
    self.assertEqual(Author.objects.get().name, 'Ged Ira')

class BookTest(APITestCase):
  
  def setUp(self) -> None:
    User = get_user_model()
    self.user = User.objects.create_user(username='lauren',email='' ,password='secret123')
    self.author = Author.objects.create(name = 'Ged Ira')
    self.book = Book.objects.create(
      title = 'Test Book',
      author = self.author,
      publication_year = 2000
    )
    
    self.client = APIClient()
    self.client.login(username='lauren', password='secret123')
    
  def test_book_retrieval(self):
    self.url = reverse('book_detail', args=[self.book.pk])
    response = self.client.get(self.url, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['title'], 'Test Book')
    self.assertEqual(response.data['author'], 1)
    self.assertEqual(response.data['publication_year'], 2000) 


  def test_book_delete(self):
    url = reverse('book_delete', args=[self.book.pk])
    response = self.client.delete(url)
    
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
  def test_book_update(self):
    data = {"publication_year" : 2003}
    url = reverse('book_update', args=[self.book.pk])
    response = self.client.patch(url, data, format='json')
    
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['publication_year'], 2003)
    
  def tearDown(self) -> None:
    self.client.logout
  
    