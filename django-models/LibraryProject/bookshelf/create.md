from bookshelf.models import Book
new_book = Book.objects.create(title = "1984", author = "George Orwell", publication_year = 1949)
#  no out put 