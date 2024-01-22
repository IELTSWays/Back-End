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



class PaymentVerify(APIView):
    @transaction.atomic
    def get(self, *args, **kwargs):
        status = self.request.query_params.get("Status")
        authority = self.request.query_params.get("Authority")
        id = kwargs.get("id")

        if not authority or status != "OK":
            return redirect('https://panel.istroco.com/payment/faild')

        try:
            invoice = Invoice.objects.get(id=id, status="پرداخت نشده")
        except Invoice.DoesNotExist:
            return bad_request("Invoice does not exist or already paid.")

        data = {
            "MerchantID": settings.ZARRINPAL_MERCHANT_ID,
            "Amount": invoice.price,
            "Authority": authority,
        }
        data = json.dumps(data)
        headers = {'content-type': 'application/json', 'content-length': str(len(data))}
        response = requests.post(settings.ZP_API_VERIFY, data=data, headers=headers)

        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                invoice.status = "پرداخت شده"
                invoice.authority = authority
                invoice.ref_id = response['RefID']
                invoice.save()
                return redirect('https://panel.istroco.com/payment/success/?RefID={}'.format(response['RefID']))
            else:
                return SuccessResponse(data={'status': False, 'details': 'Invoice already paid' })
        return SuccessResponse(data=response.content)
