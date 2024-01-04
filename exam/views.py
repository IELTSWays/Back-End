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





class StartTest(APIView):
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = self.request.data
        data['user'] = self.request.user.id
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)





class Answer(APIView):
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        test = Test.objects.get(test_id=self.kwargs["id"])
        serialized_data = self.serializer_class(test).data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        test = Test.objects.get(test_id=self.kwargs["id"])
        data = self.request.data
        data['book'] = test.book.id
        data['user'] = test.user.id
        data['type'] = test.type
        data['skill'] = test.skill

        if self.request.user != test.user:
            return Response("You are not allowed to take this exam.",status=status.HTTP_406_NOT_ACCEPTABLE)

        if test.test_done == True:
            return Response("You are not allowed to change, the test is finished.",status=status.HTTP_406_NOT_ACCEPTABLE)

        serializer = self.serializer_class(test, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

