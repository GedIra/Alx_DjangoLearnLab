from django.contrib import admin
from .models import User, Post, UserProfile

# Register your models here.

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
  list_display = ['id', 'username', 'first_name', 'last_name', 'is_staff', 'is_active']
  list_filter = ['id', 'is_staff']
  search_fields = ['username']
  ordering = ['id']

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
  list_display = ['id', 'title', 'author', 'published_date']
  list_filter = ['author']
  search_fields = ['author', 'title', 'published_date']
  ordering = ['title']
  
class UserProfileAdmin(admin.ModelAdmin):
  list_display = ['user','dob']
  list_filter = ['user', 'dob']
  search_fields = ['user']
  ordering = ['user']
  
admin.site.register(UserProfile, UserProfileAdmin)

class CommentAdmin(admin.ModelAdmin):
  list_display = ['post', 'author', 'created_at']
  list_filter = ['post', 'author', 'created_at']
  search_fields = ['post', 'author', 'created_at']
  ordering = ['post']