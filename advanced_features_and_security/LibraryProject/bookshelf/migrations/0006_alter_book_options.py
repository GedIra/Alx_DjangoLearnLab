# Generated by Django 5.1.2 on 2024-11-28 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0005_alter_book_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('can_name', 'can give a name')]},
        ),
    ]
