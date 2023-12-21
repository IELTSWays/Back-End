from rest_framework import serializers
from teacher.models import Teacher,ReserveTimes


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class ReserveTimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReserveTimes
        fields = "__all__"



class TeachersReserveTimesSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    class Meta:
        model = ReserveTimes
        fields = "__all__"