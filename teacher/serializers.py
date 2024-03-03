from rest_framework import serializers
from teacher.models import Teacher,ReserveTimes


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"



class TeacherUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ("name","description","writing_price", "speaking_price")

class TeacherUpdatePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ("photo",)





class ReserveTimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReserveTimes
        fields = "__all__"



class TeachersReserveTimesSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    class Meta:
        model = ReserveTimes
        fields = "__all__"