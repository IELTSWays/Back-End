from exam.models import Test
from answers.models import TestCorrectAnswer
from exam.serializers import QuestionSerializer, TestSerializer
from answers.serializers import AnswerSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView


class Answer(APIView):
    serializer_class = AnswerSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        data['user'] = self.request.user.id
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)




class CorrectAnswer(APIView):
    serializer_class = AnswerSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        try:
            test = TestCorrectAnswer.objects.get(name=self.kwargs["name"])
            serialized_data = self.serializer_class(test).data
            return Response(serialized_data, status=status.HTTP_200_OK)
        except:
            return Response("Test Correct Answer not found, try again", status=status.HTTP_400_BAD_REQUEST)


