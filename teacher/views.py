from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from teacher.serializers import TeacherSerializer,ReserveTimesSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.models import User
from teacher.models import Teacher,ReserveTimes
from teacher import models


class TeacherList(APIView):
    serializer_class = TeacherSerializer
    permission_classes = [AllowAny]
    def get(self, *args, **kwargs):
        teachers = Teacher.objects.all()
        serializer = self.serializer_class(teachers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class TeacherItem(APIView):
    serializer_class = TeacherSerializer
    permission_classes = [AllowAny]
    def get(self, *args, **kwargs):
        try:
            teacher = Teacher.objects.get(id=self.kwargs["id"])
            serializer = self.serializer_class(teacher)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("teacher not found or something went wrong, try again", status=status.HTTP_400_BAD_REQUEST)



class ReserveTimes(APIView):
    serializer_class = ReserveTimesSerializer
    permission_classes = [AllowAny]
    def get(self, *args, **kwargs):
        times = models.ReserveTimes.objects.all()
        serializer = self.serializer_class(times, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

