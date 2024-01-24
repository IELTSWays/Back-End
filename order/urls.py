from django.urls import path
from order.payment_views import PaymentReq, ZarinpalVerify, ManualPayment
from order.views import CreateOrder

urlpatterns = [
    path("create-order", CreateOrder.as_view(), name="create-order"),
    #path("payment-request/<int:id>/",PaymentReq.as_view(),name="payment-request"),
    path("zarinpal-verify/<int:id>/",ZarinpalVerify.as_view(),name="zarinpal-verify"),
    path("manual_payment/<int:id>",ManualPayment.as_view(),name="manual_payment"),
]


