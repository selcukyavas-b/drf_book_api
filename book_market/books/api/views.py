from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from books.api.permissions import IsAdminUserOrReadOnly, IsCommentOwnerOrReadOnly,IsAuthorOrReadOnly
from books.api.serializers import BookSerializer, CommentSerializer, CategorySerializer

from books.models import Book, Comment, Category


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)  

class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthorOrReadOnly, permissions.IsAuthenticatedOrReadOnly]

class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        book_pk=self.kwargs.get('book_pk')
        book= get_object_or_404(Book, pk=book_pk)
        user=self.request.user
        comments=Comment.objects.filter(book=book, comment_owner=user)
        if comments.exists():
            raise ValidationError('Bir kitaba sadece bir yorum yapabilirsiniz.')

        serializer.save(book=book, comment_owner=user)

class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes=[IsCommentOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly]
    




