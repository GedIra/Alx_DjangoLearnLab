#from .models import Author, Book, Library, Librarian

author = Author.objects.create(name='George Orwell')

#Query all books by a specific author.
books = Book.objects.filter(author='George Orwell')

for book in books:
  print(book.title)

#List all books in a library.
library_name = 'Ikaze Library'
all_library_books = Library.objects.get(name=library_name)

for book in all_library_books:
  print(book.title)

#Retrieve the librarian for a library.
librarian = Librarian.objects.get(library="Ikaze Library")
print(librarian.name)



