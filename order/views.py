from django.shortcuts import render, redirect
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
from django.conf import settings
from django.db import transaction
from django.db.models import F
from config.responses import bad_request, SuccessResponse, UnsuccessfulResponse
from zibal.zb import Zibal as zb
from django.http import HttpResponse





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


        if req['payment_method'] == "zibal":

            # ------ Zibal ------------

            zb_object = zb(settings.ZIBAL_MERCHANT_ID)
            zb_data = zb_object.request(settings.ZIBAL_CALL_BACK, order.id, order.amount,
                                        "خریداری آزمون آنلاین آیلتس ویز", order.user.id)
            print('---------')
            print(zb_data.data)
            if zb_data['status'] == "successful":
                return redirect(zb_data['start_pay_url'])
            else:
                return HttpResponse(zb_data["message"])



        elif req['payment_method'] == "zarinpal":

            # ------ Zarinpal ---------

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



        else:
            pass
