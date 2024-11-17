from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=User)
def Signal_update_create_profile(sender, created, instance, **kwargs):
  if created:
    #creation 
    UserProfile.objects.create(user=instance)
    logger.info(f"Created UserProfile for user: {instance.username}")
  
  else:
    #Updating
    instance.userprofile.save()
    logger.info(f"Updated UserProfile for user: {instance.username}")
