from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.functions import get_user_data, login
from accounts.models import OneTimePassword
from accounts.selectors import get_user
from config.settings import ACCESS_TTL
from accounts.serializers import UserSerializer, UserAllFieldsSerializer, UserUpdateSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
import re
from django.utils.translation import gettext as _
from rest_framework.throttling import AnonRateThrottle
from accounts.functions import send_sms_otp
from accounts.models import OneTimePassword, User




class Profile(APIView):
    serializer_class = UserAllFieldsSerializer
    permission_classes = [AllowAny]

    def get(self, *args, **kwargs):
        profile = User.objects.get(id=self.request.user.id)
        serializer = self.serializer_class(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        profile = User.objects.get(id=self.request.user.id)
        serializer = UserUpdateSerializer(profile, data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


