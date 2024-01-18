from rest_framework import serializers
from answers.models import TestCorrectAnswer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCorrectAnswer
        fields = "__all__"


