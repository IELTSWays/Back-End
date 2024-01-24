from django.urls import path
from order.payment_views import ZarinpalPaymentReq, ZarinpalVerify, ManualPayment
from order.views import CreateOrder, CreateOrderNoPay

urlpatterns = [
    path("create-order", CreateOrder.as_view(), name="create-order"),
    path("create-order-nopay", CreateOrderNoPay.as_view(), name="create-order-nopay"),
    path("zarinpal-request/<int:id>/",ZarinpalPaymentReq.as_view(),name="zarinpal-request"),
    path("zarinpal-verify/<int:id>/",ZarinpalVerify.as_view(),name="zarinpal-verify"),
    path("manual_payment/<int:id>",ManualPayment.as_view(),name="manual_payment"),
]


