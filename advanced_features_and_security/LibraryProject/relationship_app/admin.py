from django.contrib import admin
from .models import Author, Book, Library, Librarian, UserProfile

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
  list_display = ("name",)
  list_filter = ("name",)
  search_fields = ('name',)

class BookAdmin(admin.ModelAdmin):
  list_display = ("title", "author",)
  list_filter = ("author",)
  search_fields = ('title', 'author',)

class LibraryAdmin(admin.ModelAdmin):
  list_display = ("name",)
  list_filter = ("name", "books",)
  search_fields = ('name',)

class UserProfileAdmin(admin.ModelAdmin):
  list_display = ("user", "role",)
  list_filter = ('role',)
  search_fields = ('role',)

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Library, LibraryAdmin)

