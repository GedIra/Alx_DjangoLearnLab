from rest_framework import serializers
from .models import User
from rest_framework.response import Response

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', 'followers', 'following', 'bio', 'profile_picture' ]
    
class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'password', 'email']
    extra_kwargs = {'password': {'write_only': True}}
    
  def create(self, validated_data):
    user = User.objects.create_user(
      username = validated_data['username'],
      password = validated_data['password'],
      email = validated_data['email'],
    )
    return user
    

    
    