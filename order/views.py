from django.shortcuts import render
from order.serializers import OrderSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.models import User
from order.models import Order
from exam.models import TestPrice, Test
from book.models import Book
import json
import requests
from django.shortcuts import redirect
from django.conf import settings
from django.db import transaction
from django.db.models import F
from config.responses import bad_request, SuccessResponse, UnsuccessfulResponse






class CreateOrder(APIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def post(self, *args, **kwargs):
        req = self.request.data

        # create Order:

        amount = 0
        for test in req['test']:

            if test[4] == "L":
                price = TestPrice.objects.get(id=1).listening
                amount += price

            if test[4] == "R":
                price = TestPrice.objects.get(id=1).reading
                amount += price

            if test[4] == "W":
                price = 0
                amount += price

            if test[4] == "S":
                price = 0
                amount += price

        order = Order()
        order.amount = amount
        order.user = self.request.user
        order.description = req['test']
        order.save()

        authority = self.request.query_params.get("Authority")
        status = self.request.query_params.get("Status")
        id = kwargs.get("id")

        data = {
            "MerchantID": settings.ZARRINPAL_MERCHANT_ID,
            "Amount": order.amount,
            "Description": "خریداری آزمون آنلاین آیلتس ویز",
            "Authority": authority,
            "CallbackURL": settings.ZARIN_CALL_BACK + str(order.id) + "/",
            "OrderID": order.id,
        }
        data = json.dumps(data)
        headers = {'content-type': 'application/json', 'content-length': str(len(data))}

        try:
            response = requests.post(settings.ZP_API_REQUEST, data=data, headers=headers, timeout=10)

            if response.status_code == 200:
                response = response.json()
                if response['Status'] == 100:
                    order.authority = response['Authority']
                    order.save()
                    order_serializer = OrderSerializer(order)
                    data = {'status': True, 'url': settings.ZP_API_STARTPAY + str(response['Authority']),
                            'order': order.id, 'authority': response['Authority']}
                    return SuccessResponse(order_serializer.data, data)
                else:
                    return {'status': False, 'code': str(response['Status'])}
            return response

        except requests.exceptions.Timeout:
            return {'status': False, 'code': 'timeout'}
        except requests.exceptions.ConnectionError:
            return {'status': False, 'code': 'connection error'}


        ''' 

        #create tests:

        for test in req['test']:

            if test[3] == "A":
                type = "academic"
            else:
                type = "general"


            if test[4] == "L":
                skill = "listening"
            elif test[4] == "R":
                skill = "reading"
            elif test[4] == "W":
                skill = "writing"
            else:
                skill = "speaking"

            test_book = Book.objects.get(id=int(test[1]+test[2]))
            test_name =  test[0]+test[1]+test[2]+test[4]+test[5]+test[6]

            answers = {
                "00001": None,
                "00002": None,
                "00003": None,
                "00004": None,
                "00005": None,
                "00006": None,
                "00007": None,
                "00008": None,
                "00009": None,
                "00010": None,
                "00011": None,
                "00012": None,
                "00013": None,
                "00014": None,
                "00015": None,
                "00016": None,
                "00017": None,
                "00018": None,
                "00019": None,
                "00020": None,
                "00021": None,
                "00022": None,
                "00023": None,
                "00024": None,
                "00025": None,
                "00026": None,
                "00027": None,
                "00028": None,
                "00029": None,
                "00030": None,
                "00031": None,
                "00032": None,
                "00033": None,
                "00034": None,
                "00035": None,
                "00036": None,
                "00037": None,
                "00038": None,
                "00039": None,
                "00040": None}

            test = Test()
            test.user = self.request.user
            test.skill = skill
            test.type = type
            test.book = test_book
            test.answers = answers
            test.name = test_name
            test.save()

            print(test.test_id)

            #if pardakht ok bood test haro ijad kon va id ro bede
            
        '''

