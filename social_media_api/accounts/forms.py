from django import forms
from .models import User
from django.core.exceptions import ValidationError
class UserCreationForm(forms.ModelForm):
  password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
  password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
  
  class Meta:
    model = User
    fields = ['username', 'email']
    
  def clean_password2(self):
    password1 = self.cleaned_data.get("password1")
    password2 = self.cleaned_data.get("password2")
    
    if password1 and password2 and password1 != password2:
      raise ValidationError("Password mismatch !")
    
    return password2
  
  def save(self, commit = True):
    # Save the provided password in hashed format
    user = super().save(commit=False)
    user.set_password(self.cleaned_data['password1'])
    if commit:
      user.save()
    return user

  


    
    
    