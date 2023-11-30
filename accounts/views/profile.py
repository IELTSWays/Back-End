from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.functions import get_user_data, login
from accounts.models import OneTimePassword
from accounts.selectors import get_user
from config.settings import ACCESS_TTL
from accounts.serializers import UserSerializer, ChangePhoneSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
import re
from django.utils.translation import gettext as _
from rest_framework.throttling import AnonRateThrottle
from accounts.functions import send_sms_otp, send_sms_pass
from accounts.models import OneTimePassword, User




class Profile(APIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        profile = User.objects.get(id=self.request.user.id)
        serializer = UserSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        profile = User.objects.get(id=self.request.user.id)
        self.request.data['phone_number'] = profile.phone_number
        serializer = UserSerializer(profile, data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)





phone_number_regex = re.compile(r"^09\d{9}")
class ChangePhone(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, *args, **kwargs):
        phone_number = self.request.data.get("phone_number")
        if not phone_number_regex.match(phone_number):
            return Response({"success": False, "errors": [_("invalid phone number")]},status=status.HTTP_400_BAD_REQUEST,)
        if OneTimePassword.otp_exist(phone_number):
            return Response({"success": False, "errors": [_("otp already sent")]},status=status.HTTP_400_BAD_REQUEST,)
        if User.objects.filter(phone_number=phone_number).exists():
            return Response({"success": False, "errors": [_("user with this phone number already exists")]},status=status.HTTP_400_BAD_REQUEST,)

        otp = OneTimePassword(self.request.user)
        print(otp.code)
        done = send_sms_otp(phone_number, otp.code)

        if not done:
            return Response({"success": False, "errors": [_("error in sending otp")]},status=status.HTTP_400_BAD_REQUEST)
        return Response({"success": True, "data": {"otp_id": otp.otp_id}, }, status=status.HTTP_200_OK)



class ChangePhoneVerifyOTP(APIView):
    permission_classes = []

    def post(self, *args, **kwargs):
        otp_id = self.request.data.get("otp_id", "")
        otp_code = self.request.data.get("otp_code", "")
        try:
            user_id = OneTimePassword.verify_otp(otp_id, otp_code)
        except ValueError:
            return Response({"success": False, "errors": [_("OTP is invalid")]},status=status.HTTP_400_BAD_REQUEST,)

        try:
            user = get_user(id=user_id)
        except:
            return Response({"success": False, "errors": [_("User not found")]},status=status.HTTP_400_BAD_REQUEST)

        try:
            user.phone_number = self.request.data.get("phone_number", "")
            user.save()
            return Response({"success": True, "data": "User phone number changed successfully."},status=status.HTTP_200_OK)
        except:
            return Response({"success": False, "errors": [_("Something went wrong,")]},status=status.HTTP_400_BAD_REQUEST)
