from django.contrib import admin
from books.models import Book, Comment, Category

# Register your models here.

admin.site.register(Book)
admin.site.register(Comment)
admin.site.register(Category)
