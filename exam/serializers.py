from rest_framework import serializers
from exam.models import Test, WritingTest, SpeakingTest


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"


class AnswerSerializer(serializers.Serializer):
    test_done = serializers.BooleanField()
    answers = serializers.JSONField()


class QuestionSerializer(serializers.Serializer):
    number = serializers.IntegerField()
    type = serializers.CharField()
    question = serializers.CharField()
    answer = serializers.CharField()
    image = serializers.CharField()
    text = serializers.CharField()






class WritingTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = WritingTest
        fields = "__all__"



class SpeakingTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeakingTest
        fields = "__all__"