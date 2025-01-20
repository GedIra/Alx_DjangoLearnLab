from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ['url','username', 'email', 'first_name', 'last_name', 'followers', 'following', 'bio', 'profile_picture' ]
    
class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'password', 'email']
    extra_kwargs = {'password': {'write_only': True}}
    
  def create(self, validated_data):
    user = get_user_model().objects.create_user(
      username = validated_data['username'],
      password = validated_data['password'],
      email = validated_data['email'],
    )
    Token.objects.create(user=user)
    return user
    

#serializers.CharField()

    

    
    

    