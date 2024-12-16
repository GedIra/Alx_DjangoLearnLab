from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import HttpResponse
from .models import UserProfile, User, Post, Comment


class UserCreationForm(forms.ModelForm):
  
  password1 = forms.CharField(label="password", widget=forms.PasswordInput)
  password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)
  
  class Meta:
    model = User
    fields = ['username', 'email']
    
    
  def clean_password2(self):
    # Check that the two password entries match
    password1 = self.cleaned_data.get("password1")
    password2 = self.cleaned_data.get("password2")
    
    if password1 and password2 and password2 != password1:
      raise ValidationError("Passwords mismatch !") 
    return password2
  
  def save(self, commit = True):
    # Save the provided password in hashed format
    user = super().save(commit=False)
    user.set_password(self.cleaned_data['password1'])
    if commit:
      user.save()
    return user
  
class LoginForm(forms.Form):
  username = forms.CharField(max_length=30)
  password = forms.CharField(widget=forms.PasswordInput)

    
class UserProfileForm(forms.ModelForm):
  email = forms.EmailField(required=True)

  class Meta:
    model = UserProfile
    fields = ['picture', 'dob', 'bio']

  def __init__(self, *args, **kwargs):
    super(UserProfileForm, self).__init__(*args, **kwargs)
    if self.instance and self.instance.user:
      self.fields['email'].initial = self.instance.user.email


    # Apply CSS classes and attributes
    self.fields['email'].widget.attrs.update({'class': 'form-control'})
    self.fields['picture'].widget.attrs.update({'class': 'form-control'})
    self.fields['dob'].widget.attrs.update({'class': 'form-control', 'placeholder': 'YYYY-MM-DD'})
    self.fields['bio'].widget.attrs.update({'class': 'form-control', 'rows': 5})

  def save(self, commit=True):
    user_profile = super(UserProfileForm, self).save(commit=False)
    user_profile.user.email = self.cleaned_data['email']
    if commit:
        user_profile.user.save()
        user_profile.save()
    return user_profile

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    exclude = ['author']
    
class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['content',]
    exclude = ['author', 'post']
    