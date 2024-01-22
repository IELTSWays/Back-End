from django.urls import path
from order.payment_views import PaymentReq, PaymentVerify
from order.views import CreateOrder

urlpatterns = [
    path("create-order", CreateOrder.as_view(), name="create-order"),
    path("payment-request/<int:id>/",PaymentReq.as_view(),name="payment-request"),
    path("payment-verify/<int:id>/",PaymentVerify.as_view(),name="payment-verify"),
]


