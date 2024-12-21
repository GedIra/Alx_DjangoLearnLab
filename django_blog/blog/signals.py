from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import UserProfile, User

@receiver(post_save, sender= User)
def create_user_profile(sender, instance, created, **kwargs):
  """Create a user profile if the user is created"""
  if created:
    user_profile = UserProfile.objects.create(user=instance)
    user_profile.save()