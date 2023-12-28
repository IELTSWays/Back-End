from exam.models import Test
from exam.serializers import QuestionSerializer, TestSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView


class AddQuestion(APIView):
    serializer_class = TestSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        test = Test.objects.get(id=self.kwargs["id"])
        serialized_data = self.serializer_class(test).data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        test = Test.objects.get(id=request.data['test_id'])
        test.questions = request.data['questions']
        test.save()
        return Response("questions added", status=status.HTTP_200_OK)

