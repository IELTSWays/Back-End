from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from book.serializers import BookSerializer, ProductSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.models import User
from book.models import Book, Product



class Products(APIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    def get(self, *args, **kwargs):
        books = Book.objects.all()
        products = Product.objects.all()

        for book in books:
            for product in products:

                if product.book == book:

                    if product.id[3] == "L":
                        skill = "listening"
                    if product.id[3] == "W":
                        skill = "writing"
                    if product.id[3] == "R":
                        skill = "reading"


                    for i in range(1,5):
                        if str(product.id[5]) == str(i):
                            item = {"id":product.id, "type":product.type, "skill":skill}
                            print(item)

        aaa = {"book": BookSerializer(book).data, "tests": testss}


        #serializer = self.serializer_class(products, many=True)
        return Response(aaa, status=status.HTTP_200_OK)




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

