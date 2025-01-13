from django import forms
from bookshelf.models import Book
from django.contrib.auth import get_user_model

User = get_user_model()

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

class ExampleForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'date_of_birth','profile_photo']
        
    