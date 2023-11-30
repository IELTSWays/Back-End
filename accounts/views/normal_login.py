from django.utils.translation import gettext as _
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.functions import get_user_data, login
from config.settings import ACCESS_TTL
from accounts.serializers import UserSerializer
from django.contrib.auth import authenticate


class NormalLogin(APIView):
    permission_classes = []

    def post(self, *args, **kwargs):
        phone_number = self.request.data.get("phone_number")
        password = self.request.data.get("password")
        user = authenticate(phone_number=phone_number, password=password)
        if user is not None:
            access, refresh = login(user)
            data = {
                "refresh_token": refresh,
                #"access_token": access,
                "user_type": user.user_type,
                "user_data": UserSerializer(user).data}
            response = Response( {"success": True, "data": data}, status=status.HTTP_200_OK)
            response.set_cookie(
                "HTTP_ACCESS",
                f"Bearer {access}",
                max_age=ACCESS_TTL * 24 * 3600,
                secure=True,
                httponly=True,
                samesite="None",
            )
            return response

        else:
            return Response({"success": False, "errors": [_("Phone number or password is incorrect")]},status=status.HTTP_400_BAD_REQUEST)
