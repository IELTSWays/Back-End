from django.shortcuts import render, redirect
from django.conf import settings
from django.views.generic.base import View
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from accounts.models import User
from config import responses
from rest_framework import status
from rest_framework.response import Response
import requests
from accounts.functions import get_user_data, login
from accounts.models import OneTimePassword
from accounts.selectors import get_user
from config.settings import ACCESS_TTL
from accounts.serializers import UserSerializer
from django.utils.translation import gettext as _
from accounts.utils import random_N_chars_str, random_with_N_digits


def index(request):
    return render(request, 'index.html')



class GoogleAuthRedirect(View):
    permission_classes = [AllowAny]
    def get(self, request):
        redirect_url = f"https://accounts.google.com/o/oauth2/v2/auth?client_id={settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY}&response_type=code&scope=https://www.googleapis.com/auth/userinfo.profile%20https://www.googleapis.com/auth/userinfo.email&access_type=offline&redirect_uri=http://127.0.0.1:8000/google-redirect/"
        return redirect(redirect_url)



class GoogleRedirectURIView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        # Extract the authorization code from the request URL
        code = self.request.GET.get('code')

        if code:
            # Prepare the request parameters to exchange the authorization code for an access token
            token_endpoint = 'https://oauth2.googleapis.com/token'
            token_params = {
                'code': code,
                'client_id': settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY,
                'client_secret': settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET,
                'redirect_uri': 'http://127.0.0.1:8000/google-redirect/',
                # Must match the callback URL configured in your Google API credentials
                'grant_type': 'authorization_code',
            }

            # Make a POST request to exchange the authorization code for an access token
            response = requests.post(token_endpoint, data=token_params)

            if response.status_code == 200:
                access_token = response.json().get('access_token')

                if access_token:
                    # Make a request to fetch the user's profile information
                    profile_endpoint = 'https://www.googleapis.com/oauth2/v1/userinfo'
                    headers = {'Authorization': f'Bearer {access_token}'}
                    profile_response = requests.get(profile_endpoint, headers=headers)

                    if profile_response.status_code == 200:
                        data = {}
                        profile_data = profile_response.json()
                        # Proceed with user creation or login
                        random_num = '09{}'.format(random_with_N_digits(9))
                        user = User.objects.create_user(first_name=profile_data["given_name"], email=profile_data["email"], phone_number=random_num)
                        if "family_name" in profile_data:
                            user.last_name = profile_data["family_name"]
                            user.save()
                        user.wrong_phone=True
                        user.save()
                        access, refresh = login(user)

                        data = {
                            "refresh_token": refresh,
                            "access_token": access,
                            "user_data": UserSerializer(user).data,
                        }
                        response = Response(
                            {
                                "success": True,
                                "data": data,
                            },
                            status=status.HTTP_200_OK,
                        )
                        response.set_cookie(
                            "HTTP_ACCESS",
                            f"Bearer {access}",
                            max_age=ACCESS_TTL * 24 * 3600,
                            secure=True,
                            httponly=True,
                            samesite="None",)
                        return response

        return Response({}, status.HTTP_400_BAD_REQUEST)