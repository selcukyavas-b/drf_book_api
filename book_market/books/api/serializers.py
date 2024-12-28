from rest_framework import serializers
from books.models import Book, Comment, Category
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


# class CustomRegisterSerializer(RegisterSerializer):
#     username = None
#     def validate_email(self, email):
#         email = email.lower()
#         if User.objects.filter(email=email).exists():
#             raise serializers.ValidationError(_("This email is already in use."))
#         return email



class CommentSerializer(serializers.ModelSerializer):
    comment_owner=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Comment
        exclude=['book']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields ='__all__'

class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    comments= CommentSerializer(many=True, read_only=True)
    categories = serializers.SlugRelatedField(
        slug_field='name', queryset=Category.objects.all(), many=True
    )

    class Meta:
        model=Book
        fields='__all__'    