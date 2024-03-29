from rest_framework import serializers
from book.models import Book, Product


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"



class ProductSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    class Meta:
        model = Product
        fields = "__all__"
