from django.urls import path
from order.payment_views import ZarinpalPaymentReq, ZarinpalVerify, ManualPayment,SpeakingManualPay,ZarinpalSpeakingReq,ZarinpalSpeakingVerify, WritingManualPay,ZarinpalWritingReq, ZarinpalWritingVerify
from order.views import CreateOrder, CreateOrderNoPay, UserOrders

urlpatterns = [
    path("user-orders", UserOrders.as_view(), name="user-orders"),
    path("create-order", CreateOrder.as_view(), name="create-order"),
    path("create-order-nopay", CreateOrderNoPay.as_view(), name="create-order-nopay"),
    path("zarinpal-request/<int:id>/",ZarinpalPaymentReq.as_view(),name="zarinpal-request"),
    path("zarinpal-verify/<int:id>/",ZarinpalVerify.as_view(),name="zarinpal-verify"),
    path("manual_payment/<int:id>",ManualPayment.as_view(),name="manual_payment"),
    path("zarinpal-speaking-req/<int:id>/",ZarinpalSpeakingReq.as_view(),name="zarinpal-speaking-req"),
    path("zarinpal-speaking-verify/<int:id>/",ZarinpalSpeakingVerify.as_view(),name="zarinpal-speaking-verify"),
    path("speaking-manual-pay/<int:id>",SpeakingManualPay.as_view(),name="speaking-manual-pay"),
    path("zarinpal-writing-req/<int:id>/",ZarinpalWritingReq.as_view(),name="zarinpal-writing-req"),
    path("zarinpal-writing-verify/<int:id>/",ZarinpalWritingVerify.as_view(),name="zarinpal-writing-verify"),
    path("writing-manual-pay/<int:id>",WritingManualPay.as_view(),name="writing-manual-pay"),
]


