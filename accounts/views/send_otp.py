import re
from django.utils.translation import gettext as _
from rest_framework import status
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.views import APIView
from accounts.functions import send_sms_otp, send_tele_otp
from accounts.models import OneTimePassword, User
from django.http import HttpResponse
from telegram import Bot
import asyncio
import requests
#import telebot

phone_number_regex = re.compile(r"^09\d{9}")


class OTPThrottle(AnonRateThrottle):
    scope = "otp"


class SendOTP(APIView):
    permission_classes = []
    # throttle_classes = [OTPThrottle]

    def post(self, *args, **kwargs):
        phone_number = self.request.data.get("phone_number")
        if not phone_number_regex.match(phone_number):
            return Response(
                {"success": False, "errors": [_("invalid phone number")]},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if OneTimePassword.otp_exist(phone_number):
            return Response(
                {"success": False, "errors": [_("otp already sent")]},
                status=status.HTTP_400_BAD_REQUEST,
            )


        if User.objects.filter(phone_number=phone_number).exists():
            user = User.objects.get(phone_number=phone_number)
        else:
            user = User.objects.create_user(phone_number=phone_number)

        otp = OneTimePassword(user)
        print('---- OTP ----')
        print(otp.code)

        done = send_sms_otp(phone_number, otp.code)
        if not done:
            return Response(
                {"success": False, "errors": [_("error in sending otp")]},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            {
                "success": True,
                "data": {"otp_id": otp.otp_id},
            },
            status=status.HTTP_200_OK,
        )




class SendOTPTelegram(APIView):
    permission_classes = []
    # throttle_classes = [OTPThrottle]

    def post(self, *args, **kwargs):
        phone_number = self.request.data.get("phone_number")
        if not phone_number_regex.match(phone_number):
            return Response(
                {"success": False, "errors": [_("invalid phone number")]},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if OneTimePassword.otp_exist(phone_number):
            return Response(
                {"success": False, "errors": [_("otp already sent")]},
                status=status.HTTP_400_BAD_REQUEST,
            )


        if User.objects.filter(phone_number=phone_number).exists():
            user = User.objects.get(phone_number=phone_number)
        else:
            user = User.objects.create_user(phone_number=phone_number)

        otp = OneTimePassword(user)
        print('---- OTP ----')
        print(otp.code)
        code = str(otp.code)



        bot = telebot.TeleBot('6589901044:AAFl2ct4kggaT-rZR0rtEkfAKJ6VS1OvZuk')
        chat_id = 'dorostkarnima'
        message = 'hiiii'
        bot.send_message(chat_id, message)



        '''
        bot_token = '6589901044:AAFl2ct4kggaT-rZR0rtEkfAKJ6VS1OvZuk'
        bot_chatID = 'dorostkarnima'
        bot_message = 'hiiiii'
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)
        return response.json()
        '''

        #send_tele_otp()

        return Response({"success": True,"data": {"otp_id": otp.otp_id}}, status=status.HTTP_200_OK)




