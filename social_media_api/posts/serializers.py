from .models import Post, Comment
from rest_framework import serializers

class CommentSerializer(serializers.HyperlinkedModelSerializer):
  post= serializers.HyperlinkedRelatedField(view_name='post-detail', read_only = True)
  post_title = serializers.CharField(source='post.title')
  class Meta:
    model = Comment
    fields = ['url', 'author', 'post_title', 'post', 'content', 'created_at', 'updated_at']
    read_only_fields = ['author', 'post_title', 'created_at', 'updated_at']


class PostSerializer(serializers.HyperlinkedModelSerializer):
  author_name = serializers.CharField(source='author.username')
  date = serializers.SerializerMethodField()
  comments = serializers.HyperlinkedRelatedField(many=True, view_name='comment-detail', read_only=True)
  class Meta:
    model = Post
    fields = ['url','title', 'content', 'author_name','date', 'comments']
    read_only_fields = ['date', 'author_name']
    
  def get_date(self, obj):
    return obj.published_date.strftime('On %A %d-%m-%Y %H:%M:%S') if obj.published_date else None