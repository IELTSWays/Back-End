from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from book.serializers import BookSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.models import User
from book.models import Book



class BooksList(APIView):
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    def get(self, *args, **kwargs):
        books = Book.objects.all()
        serializer = self.serializer_class(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




class BookItem(APIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):
        try:
            book = Book.objects.get(id=self.kwargs["id"])
            serializer = self.serializer_class(book)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("book not found or something went wrong, try again", status=status.HTTP_400_BAD_REQUEST)

