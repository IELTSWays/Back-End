from django.urls import path
from accounts.views import ( Logout,Profile,Refresh,RefreshAccess,Register,SendOTP,VerifyOTP,UserValidationView,
                             NormalLogin,NewPass,ChangePass,ForgotPassSendOTP,ForgotPassVerifyOTP,OverView,ChangePhone,
                             ChangePhoneVerifyOTP,ChangePassword,NormalValidationView,AdminValidationView,StaffValidationView )

urlpatterns = [
    path("user/otp", SendOTP.as_view(), name="send_otp"),
    path("user/otp/verify", VerifyOTP.as_view(), name="verify_otp"),
    path("refresh", Refresh.as_view(), name="refresh"),
    path("refresh-access", RefreshAccess.as_view(), name="refresh-access"),
    path("user/register", Register.as_view(), name="register"),
    path("user/logout", Logout.as_view(), name="logout"),
    path("user/profile", Profile.as_view(), name="profile"),
    path("user/overview", OverView.as_view(), name="overview"),
    path("user/login", NormalLogin.as_view(), name="user-login"),
    path("user/new-pass", NewPass.as_view(), name="new-pass"),
    path("user/forgot-pass-otp", ForgotPassSendOTP.as_view(), name="forgot-pass-otp"),
    path("user/otp/forgot-pass-verify", ForgotPassVerifyOTP.as_view(), name="forgot-pass-verify"),
    path("user/change-pass", ChangePass.as_view(), name="change-pass"),
    path("user/chnage-phone", ChangePhone.as_view(), name="chnage-phone"),
    path("user/chnage-phone-verify", ChangePhoneVerifyOTP.as_view(), name="chnage-phone-verify"),
    path("user/chnage-password", ChangePassword.as_view(), name="change-password"),
    path("user/user-is-valid", UserValidationView.as_view(), name="is-valid"),
    path("user/normal-is-valid", NormalValidationView.as_view(), name="normal-is-valid"),
    path("user/admin-is-valid", AdminValidationView.as_view(), name="admin-is-valid"),
    path("user/staff-is-valid", StaffValidationView.as_view(), name="staff-is-valid"),
]


