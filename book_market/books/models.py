from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'

    

class Book(models.Model):
    name=models.CharField(max_length=255)
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_book')
    categories=models.ManyToManyField('Category',related_name='books')
    explanation=models.TextField(blank=True, null=True)
    creation_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
  

    def __str__(self):
        return f'{self.name} - {self.author}'
    

class Comment(models.Model):
    book=models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')

    comment_owner=models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')

    comment=models.TextField(blank=True, null=True)
    creation_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    rating=models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],


    )

    def __str__(self):
        return str(self.rating)

