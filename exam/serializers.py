from rest_framework import serializers
from exam.models import Test, WritingTest, SpeakingTest, TestHistory, Note
from teacher.serializers import TeacherSerializer, ReserveTimesSerializer
from accounts.serializers import UserSerializer

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        #fields = "__all__"
        fields = ("id", "test_id", "name", "skill", "type", "user", "book", "created_at", "is_expired", "confirm", "confirm_at", "test_done", "answers")


class ShortTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ("id", "test_id", "name", "skill", "type")


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
    marker = TeacherSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = WritingTest
        fields = "__all__"
        fields = ("id", "test_id", "name", "status", "type", "user", "marker", "test_done", "created_at", "is_expired", "confirm", "confirm_at",
        "score", "task1", "task2", "amount", "description", "authority", "ref_id", "payment_method")




class WritingCreateTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = WritingTest
        fields = "__all__"


class SpeakingTestSerializer(serializers.ModelSerializer):
    time = ReserveTimesSerializer(read_only=True)
    teacher = TeacherSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = SpeakingTest
        fields = "__all__"



class SpeakingCreateTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeakingTest
        fields = "__all__"



class TestHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TestHistory
        fields = "__all__"



class NoteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    test = ShortTestSerializer(read_only=True)
    class Meta:
        model = Note
        fields = "__all__"


class CreateNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"