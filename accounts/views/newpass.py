from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
import re
from django.utils.translation import gettext as _
from rest_framework.throttling import AnonRateThrottle
from accounts.functions import send_sms_otp, send_sms_pass
from accounts.models import OneTimePassword, User
from config import responses
from accounts.functions import get_user_data, login
from accounts.selectors import get_user
from config.settings import ACCESS_TTL
from accounts.serializers import UserSerializer
from django.contrib.auth.hashers import check_password



class ChangePassword(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, *args, **kwargs):
        try:
            current = self.request.data["current_pass"]
            new = self.request.data["new_pass"]
            user = self.request.user

            matchcheck = check_password(current, user.password)
            if matchcheck:
                user.set_password(new)
                user.save(update_fields=['password'])
                return Response('Password changed successfully.', status=status.HTTP_200_OK)
            else:
                return Response('The current password you entered is incorrect.', status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response('something went wrong please try again', status=status.HTTP_400_BAD_REQUEST)






class ChangePass(APIView):
    permission_classes = [AllowAny]

    def post(self, *args, **kwargs):
        otp_id = self.request.GET.get("id")
        otp_code = self.request.GET.get("code")

        try:
            user_id = OneTimePassword.verify_otp(otp_id, otp_code)
        except ValueError:
            return Response(
                {"success": False, "errors": [_("OTP is invalid")]},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user = get_user(id=user_id)

        try:
            password = self.request.data.get("password")
            user.set_password(password)
            user.save(update_fields=['password'])
            return Response('password changed successfully', status=status.HTTP_200_OK)
        except:
            return Response('something went wrong please try again', status=status.HTTP_400_BAD_REQUEST)



class NewPass(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, *args, **kwargs):
        try:
            password = self.request.data.get("password")
            user = self.request.user
            user.set_password(password)
            user.save(update_fields=['password'])
            return Response('password changed successfully', status=status.HTTP_200_OK)
        except:
            return Response('something went wrong please try again', status=status.HTTP_400_BAD_REQUEST)





phone_number_regex = re.compile(r"^09\d{9}")

class ForgotPassSendOTP(APIView):
    permission_classes = []
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
        try:
            user = User.objects.get(phone_number=phone_number)
        except:
            return Response({"success": False, "errors": [_("User not found")]},status=status.HTTP_400_BAD_REQUEST)

        otp = OneTimePassword(user)
        print(otp.code)
        done = send_sms_otp(phone_number, otp.code)
        print(otp.code)
        if not done:
            return Response({"success": False, "errors": [_("error in sending otp")]},status=status.HTTP_400_BAD_REQUEST)
        return Response({"success":True,"data":{"otp_id": otp.otp_id},},status=status.HTTP_200_OK)





class ForgotPassVerifyOTP(APIView):
    permission_classes = []

    def post(self, *args, **kwargs):
        otp_id = self.request.data.get("otp_id", "")
        otp_code = self.request.data.get("otp_code", "")
        try:
            user_id = OneTimePassword.verify_otp_no_delete(otp_id, otp_code)
        except ValueError:
            return Response(
                {"success": False, "errors": [_("OTP is invalid")]},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = get_user(id=user_id)
        except:
            return Response({"success": False, "errors": [_("User not found")]},status=status.HTTP_400_BAD_REQUEST)


        params = otp_id + "&code=" + otp_code   #?id= +
        link = "https://panel.istroco.com/auth/forgotPass/{}".format(params)   #/forgotPass/token   https://api.istroco.com/accounts/change-pass{}
        phone_number=user.phone_number

        done = send_sms_pass(phone_number, link)
        print(link)
        if not done:
            return Response({"success": False, "errors": [_("error in sending otp")]},status=status.HTTP_400_BAD_REQUEST)
        return Response( { "success": True,"data": "password reset link send to your phone." }, status=status.HTTP_200_OK )



