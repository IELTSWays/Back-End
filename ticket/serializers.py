from django.contrib.auth import get_user_model
from rest_framework import serializers
from ticket.models import Ticket


class GetTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"


class CreatTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ("user","title","description")