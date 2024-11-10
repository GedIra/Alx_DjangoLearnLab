#from .models import Author, Book, Library, Librarian

author_name = "George Orwell"

author = Author.objects.get(name=author_name)

#Query all books by a specific author.
books = Book.objects.filter(author=author_name)

for book in books:
  print(book.title)

#List all books in a library.
library_name = 'Ikaze Library'
books = Library.objects.get(name=library_name)
all_library_books = books.all()

for book in all_library_books:
  print(book.title)

#Retrieve the librarian for a library.
librarian = Librarian.objects.get(library="Ikaze Library")
print(librarian.name)



