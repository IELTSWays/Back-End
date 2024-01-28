from django.urls import path
from book.views import BooksList, BookItem, Products

urlpatterns = [
    path("products", Products.as_view(), name="products"),
    path("books", BooksList.as_view(), name="books"),
    path('book-item/<int:id>', BookItem.as_view(), name='book-item'),
]


