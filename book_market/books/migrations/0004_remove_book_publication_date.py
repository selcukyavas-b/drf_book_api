# Generated by Django 5.1.1 on 2024-10-16 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publication_date',
        ),
    ]
