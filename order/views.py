from django.shortcuts import render
from order.serializers import OrderSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.models import User
from order.models import Order



class CreateOrder(APIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def post(self, *args, **kwargs):
        req = self.request.data
        req['user'] = self.request.user.id
        print('--------')

        for test in req['test']:
            print(test)

        #test
        #amount


        #serializer = CreatTicketSerializer(data=req)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response('serializer.errors', status=status.HTTP_400_BAD_REQUEST)
