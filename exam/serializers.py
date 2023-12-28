from rest_framework import serializers
from exam.models import Test


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"

class QuestionSerializer(serializers.Serializer):
    number = serializers.IntegerField()
    type = serializers.CharField()
    question = serializers.CharField()
    answer = serializers.CharField()
    image = serializers.CharField()
    text = serializers.CharField()