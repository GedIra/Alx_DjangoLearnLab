# relationship_app/migrations/0006_migrate_user_data.py
from django.db import migrations
from django.conf import settings

def migrate_user_data(apps, schema_editor):
    # Get the models
    User = apps.get_model('auth', 'User')
    CustomUser = apps.get_model(settings.AUTH_USER_MODEL)

    # Migrate user data from User to CustomUser
    for user in User.objects.all():
        CustomUser.objects.create(
            id=user.id,  # Maintain the same ID
            username=user.username,
            date_of_birth=user.userprofile.date_of_birth if hasattr(user, 'userprofile') else None,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            is_staff=user.is_staff,
            is_active=user.is_active,
            is_superuser=user.is_superuser,
            date_joined=user.date_joined,
            password=user.password  # Transfer hashed password
        )

class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0001_initial'),
        ('relationship_app', '0005_alter_userprofile_role'),
    ]

    operations = [
        migrations.RunPython(migrate_user_data),
    ]

