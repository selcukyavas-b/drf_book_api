from django.urls import path, include
from books.api import views as api_views

urlpatterns = [
    path('categories/', api_views.CategoryListView.as_view(), name='category-list'),
    path('books/', api_views.BookListCreateAPIView.as_view(), name='book-list'),
    path('books/<int:pk>', api_views.BookDetailAPIView.as_view(), name='book-information'),
    path('books/<int:book_pk>/make_comment', api_views.CommentCreateAPIView.as_view(), name='make-comment'),
    path('comment/<int:pk>', api_views.CommentDetailAPIView.as_view(), name='comments'),

]