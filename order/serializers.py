from rest_framework import serializers
from order.models import Order, ManualPayment, SpeakingManualPayment


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class ManualPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManualPayment
        fields = "__all__"


class SpeakingManualPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeakingManualPayment
        fields = "__all__"

