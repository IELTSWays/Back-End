from accounts.views.logout import Logout
from accounts.views.refresh import Refresh
from accounts.views.register import Register
from accounts.views.send_otp import SendOTP
from accounts.views.verify_otp import VerifyOTP
from .user_validation import *
from accounts.views.refresh_access import RefreshAccess
from accounts.views.profile import Profile, ChangePhone, ChangePhoneVerifyOTP
from accounts.views.admin import AdminLogin, Admin, AdminItem
from accounts.views.normal_login import NormalLogin
from accounts.views.newpass import NewPass, ChangePass, ForgotPassSendOTP, ForgotPassVerifyOTP, ChangePassword
from accounts.views.overview import OverView