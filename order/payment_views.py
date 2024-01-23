#from invoice.models import Invoice
#from invoice.serializers import InvoiceSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import User
import json
import requests
from django.shortcuts import redirect
from django.conf import settings
from django.db import transaction
from django.db.models import F
from config.responses import bad_request, SuccessResponse, UnsuccessfulResponse
from django.http import HttpResponse
from order.models import Order
from book.models import Book
import ast
from exam.models import Test


class PaymentReq(APIView):
    @transaction.atomic
    def get(self, *args, **kwargs):
        authority = self.request.query_params.get("Authority")
        status = self.request.query_params.get("Status")
        id = kwargs.get("id")

        try:
            invoice = Invoice.objects.get(id=id,status="پرداخت نشده")
        except Invoice.DoesNotExist:
            return bad_request("Invoice does not exist or already paid.")

        data = {
            "MerchantID": settings.ZARRINPAL_MERCHANT_ID,
            "Amount": invoice.price,
            "Description": invoice.description,
            "Authority": authority,
            "CallbackURL": settings.ZARIN_CALL_BACK + str(invoice.id) + "/",
            "InvoiceID": invoice.id,
        }

        data = json.dumps(data)
        headers = {'content-type': 'application/json', 'content-length': str(len(data)) }

        try:
            response = requests.post(settings.ZP_API_REQUEST, data=data, headers=headers, timeout=10)

            if response.status_code == 200:
                response = response.json()
                if response['Status'] == 100:
                    invoice.authority = response['Authority']
                    invoice.save()
                    return SuccessResponse(data= {'status': True, 'url': settings.ZP_API_STARTPAY + str(response['Authority']), 'invoice': invoice.id, 'authority': response['Authority']})
                else:
                    return {'status': False, 'code': str(response['Status'])}
            return response

        except requests.exceptions.Timeout:
            return {'status': False, 'code': 'timeout'}
        except requests.exceptions.ConnectionError:
            return {'status': False, 'code': 'connection error'}



class ZarinpalVerify(APIView):
    @transaction.atomic
    def get(self, *args, **kwargs):
        status = self.request.query_params.get("Status")
        authority = self.request.query_params.get("Authority")
        id = kwargs.get("id")

        if not authority or status != "OK":
            #return redirect('https://panel.istroco.com/payment/faild')
            return HttpResponse("payment faild...", content_type='text/plain')

        try:
            order = Order.objects.get(id=id, status="new")
        except Order.DoesNotExist:
            return bad_request("Order does not exist or already paid.")

        data = {
            "MerchantID": settings.ZARRINPAL_MERCHANT_ID,
            "Amount": order.amount,
            "Authority": authority,
        }
        data = json.dumps(data)
        headers = {'content-type': 'application/json', 'content-length': str(len(data))}
        response = requests.post(settings.ZP_API_VERIFY, data=data, headers=headers)

        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                order.status = "paid"
                order.authority = authority
                order.ref_id = response['RefID']
                order.save()

                # create tests:

                new_test_ids = []
                tests = ast.literal_eval(order.description)
                for test in tests:

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

                    test_book = Book.objects.get(id=int(test[1] + test[2]))
                    test_name = test[0] + test[1] + test[2] + test[4] + test[5] + test[6]

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
                    test.user = order.user
                    test.skill = skill
                    test.type = type
                    test.book = test_book
                    test.answers = answers
                    test.name = test_name
                    test.save()

                    new_test_ids.append(test.test_id)


                #return redirect('https://panel.istroco.com/payment/success/?RefID={}'.format(response['RefID']))
                return HttpResponse("payment done... RefID={0} and your new test ids are:{1}".format(response['RefID'],new_test_ids), content_type='text/plain')
            else:
                return SuccessResponse(data={'status': False, 'details': 'order already paid' })
        return SuccessResponse(data=response.content)
