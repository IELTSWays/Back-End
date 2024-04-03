from django.shortcuts import render, redirect
from django.conf import settings
from django.views.generic.base import View
from rest_framework.permissions import AllowAny, IsAuthenticated


def index(request):
    return render(request, 'index.html')



class GoogleAuthRedirect(View):
    permission_classes = [AllowAny]
    def get(self, request):
        redirect_url = f"https://accounts.google.com/o/oauth2/v2/auth?client_id={settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY}&response_type=code&scope=https://www.googleapis.com/auth/userinfo.profile%20https://www.googleapis.com/auth/userinfo.email&access_type=offline&redirect_uri=https://protosapp.pythonanywhere.com/account/google/callback"
        return redirect(redirect_url)