from django.urls import path
from accounts.views import Logout,Profile,Refresh,RefreshAccess,OverView,SendOTP,VerifyOTP,UserValidationView,SendOTPTelegram, SendOTPWhatsApp

urlpatterns = [
    path("otp", SendOTP.as_view(), name="send_otp"),
    path("otp-telegram", SendOTPTelegram.as_view(), name="send_otp_telegram"),
    path("otp-whatsapp", SendOTPWhatsApp.as_view(), name="send_otp_whatsapp"),
    path("otp/verify", VerifyOTP.as_view(), name="verify_otp"),
    path("refresh", Refresh.as_view(), name="refresh"),
    path("refresh-access", RefreshAccess.as_view(), name="refresh-access"),
    path("logout", Logout.as_view(), name="logout"),
    path("profile", Profile.as_view(), name="profile"),
    path("overview", OverView.as_view(), name="overview"),
    path("is-valid", UserValidationView.as_view(), name="is-valid"),
]


