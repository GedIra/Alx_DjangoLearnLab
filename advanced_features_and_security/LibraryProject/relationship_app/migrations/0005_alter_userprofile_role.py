# Generated by Django 5.1.2 on 2024-11-17 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0004_alter_book_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Member', 'Member'), ('Librarian', 'Librarian')], default='Member', max_length=10, null=True),
        ),
    ]