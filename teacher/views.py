from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from teacher.serializers import TeacherSerializer,ReserveTimesSerializer, TeachersReserveTimesSerializer, TeacherUpdateSerializer, TeacherUpdatePhotoSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.models import User
from teacher.models import Teacher,ReserveTimes
from teacher import models
from datetime import datetime, timedelta


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




class TeacherReserveTimes(APIView):
    serializer_class = TeachersReserveTimesSerializer
    permission_classes = [AllowAny]
    def get(self, *args, **kwargs):
        times = models.ReserveTimes.objects.all()
        serializer = self.serializer_class(times, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)






class TeacherTimes(APIView):
    serializer_class = TeachersReserveTimesSerializer
    permission_classes = [AllowAny]
    def get(self, *args, **kwargs):
        teachers = Teacher.objects.all()
        data = []
        for teacher in teachers:
            times = models.ReserveTimes.objects.filter(teacher=teacher)
            techer = {"id":teacher.id,"name":teacher.name}
            techer_time = []
            for time in times:
                end = time.time + timedelta(minutes=20)
                if time.reserved:
                    state = "booked"
                elif time.availabe:
                    state = "selectable"
                else:
                    state = "unselectable"
                techer_times = {"full_id":str(teacher.id)+"-"+str(time.id),"id":time.id,"start":time.time,"end":end,"state":state}
                techer_time.append(techer_times)
            item = {"techer":techer, "times":techer_time}
            data.append(item)

        return Response(data, status=status.HTTP_200_OK)





class TeacherProfile(APIView):
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        teacher = Teacher.objects.get(user=self.request.user)
        serializer = self.serializer_class(teacher)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        teacher = Teacher.objects.get(user=self.request.user)
        serializer = TeacherUpdateSerializer(teacher, data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def post(self, *args, **kwargs):
        teacher = Teacher.objects.get(user=self.request.user)
        serializer = TeacherUpdatePhotoSerializer(teacher, data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)




