from exam.models import Test, TestPrice, WritingTest, SpeakingTest, TestHistory
from exam import models
from exam.serializers import QuestionSerializer, TestSerializer, AnswerSerializer,WritingCreateTestSerializer, WritingTestSerializer,SpeakingCreateTestSerializer, SpeakingTestSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from answers.models import TestCorrectAnswer
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework import pagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
import datetime
from django.utils import timezone
from teacher.models import Teacher, ReserveTimes


class CustomPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 1000



class TestPrice(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        prices = models.TestPrice.objects.get(id=1)
        price = {"listening":prices.listening,"reading":prices.reading}
        return Response(price, status=status.HTTP_200_OK)



class UserTests(GenericAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    serializer_class = TestSerializer
    #queryset = Test.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user', 'created_at', 'skill', 'type']
    search_fields = ['test_id', 'name']
    ordering_fields = ['test_id', 'created_at', 'id']

    def get(self, *args, **kwargs):
        user_tests = Test.objects.filter(user=self.request.user)
        tests = self.filter_queryset(user_tests)
        page = self.paginate_queryset(tests)
        if page is not None:
            serializer = TestSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = TestSerializer(tests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)





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




# ------- not used -------
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




class StartTestNew(APIView):
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = self.request.data
        data['user'] = self.request.user.id

        if data['skill'] == 'listening':
            skill = 'L'
        elif data['skill'] == 'reading':
            skill = 'R'
        else:
            skill = 'W'

        data['name'] = 'B'+str(data['book'])+str(skill)+'T'+str(data['test'])

        data['answers'] = {
            "00001": None,
            "00002": None,
            "00003": None,
            "00004": None,
            "00005": None,
            "00006": None,
            "00007": None,
            "00008": None,
            "00009": None,
            "00010": None,
            "00011": None,
            "00012": None,
            "00013": None,
            "00014": None,
            "00015": None,
            "00016": None,
            "00017": None,
            "00018": None,
            "00019": None,
            "00020": None,
            "00021": None,
            "00022": None,
            "00023": None,
            "00024": None,
            "00025": None,
            "00026": None,
            "00027": None,
            "00028": None,
            "00029": None,
            "00030": None,
            "00031": None,
            "00032": None,
            "00033": None,
            "00034": None,
            "00035": None,
            "00036": None,
            "00037": None,
            "00038": None,
            "00039": None,
            "00040": None }

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)




class Answer(APIView):
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            test = Test.objects.get(test_id=self.kwargs["id"])
            serialized_data = self.serializer_class(test).data
            return Response(serialized_data, status=status.HTTP_200_OK)
        except:
            return Response("Test not found, try again", status=status.HTTP_400_BAD_REQUEST)


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

        delta = timezone.now() - test.created_at
        delta_time_minutes = delta.total_seconds() / 60

        if test.skill == "listening" and delta_time_minutes >= 360:
            return Response("Your exam time is over, listening test time is 6 hours.",status=status.HTTP_406_NOT_ACCEPTABLE)

        if test.skill == "reading" and delta_time_minutes >= 480:
            return Response("Your exam time is over, reading test time is 8 hours.",status=status.HTTP_406_NOT_ACCEPTABLE)

        serializer = self.serializer_class(test, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def post(self, request, *args, **kwargs):
        test = Test.objects.get(test_id=self.kwargs["id"])

        if self.request.user != test.user:
            return Response("You are not allowed to take this exam.",status=status.HTTP_406_NOT_ACCEPTABLE)

        if test.test_done == True:
            return Response("You are not allowed to change, the test is finished.",status=status.HTTP_406_NOT_ACCEPTABLE)

        delta = timezone.now() - test.created_at
        delta_time_minutes = delta.total_seconds()/60

        if test.skill == "listening" and delta_time_minutes >= 360:
            return Response("Your exam time is over, listening test time is 6 hours.",status=status.HTTP_406_NOT_ACCEPTABLE)

        if test.skill == "reading" and delta_time_minutes >= 480:
            return Response("Your exam time is over, reading test time is 8 hours.",status=status.HTTP_406_NOT_ACCEPTABLE)

        serializer = AnswerSerializer(test, data=self.request.data)
        if serializer.is_valid():

            new_ans = test.answers
            new_ans.update(self.request.data['answers'])
            test.answers = new_ans
            test.test_done = self.request.data['test_done']
            test.save()
            serialized_data = self.serializer_class(test).data

            return Response(serialized_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)






class Report(APIView):
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            test = Test.objects.get(test_id=self.kwargs["id"])

            if self.request.user != test.user:
                return Response("You do not have permission to view this report.", status=status.HTTP_406_NOT_ACCEPTABLE)

            if test.test_done == False:
                return Response("You can't view this report, the test is not finished yet.",status=status.HTTP_406_NOT_ACCEPTABLE)

            try:
                correct_answer = TestCorrectAnswer.objects.get(name=test.name)
            except:
                return Response("Test correct answer not found.", status=status.HTTP_400_BAD_REQUEST)


            try:
                correct_answer_json_str = json.dumps(correct_answer.answers)
                correct_answer_resp = json.loads(correct_answer_json_str)
                test_answer_json_str = json.dumps(test.answers)
                test_answer_resp = json.loads(test_answer_json_str)

                raw_score = 0
                for correct_answer_key, correct_answer_value in correct_answer_resp.items():
                    for test_answer_key, test_answer_value in test_answer_resp.items():

                        if test_answer_key == correct_answer_key:
                            # print(test_answer_key, test_answer_value, correct_answer_value)

                            if type(correct_answer_value) is list:
                                for item in correct_answer_value:
                                    if test_answer_value == item:
                                        raw_score += 1

                            if test_answer_value == correct_answer_value:
                                raw_score += 1

                if test.skill == "listening":
                    if raw_score == 0:
                        band_score = 0
                    elif raw_score == 1:
                        band_score = 1
                    elif raw_score == 2:
                        band_score = 1.5
                    elif raw_score == 3:
                        band_score = 2
                    elif raw_score >= 4 and raw_score <= 5:
                        band_score = 2.5
                    elif raw_score >= 6 and raw_score <= 7:
                        band_score = 3
                    elif raw_score >= 8 and raw_score <= 9:
                        band_score = 3.5
                    elif raw_score >= 10 and raw_score <= 12:
                        band_score = 4
                    elif raw_score >= 13 and raw_score <= 15:
                        band_score = 4.5
                    elif raw_score >= 16 and raw_score <= 17:
                        band_score = 5
                    elif raw_score >= 18 and raw_score <= 22:
                        band_score = 5.5
                    elif raw_score >= 23 and raw_score <= 25:
                        band_score = 6
                    elif raw_score >= 26 and raw_score <= 29:
                        band_score = 6.5
                    elif raw_score >= 30 and raw_score <= 31:
                        band_score = 7
                    elif raw_score >= 32 and raw_score <= 34:
                        band_score = 7.5
                    elif raw_score >= 35 and raw_score <= 36:
                        band_score = 8
                    elif raw_score >= 37 and raw_score <= 39:
                        band_score = 8.5
                    else:
                        band_score = 9

                if test.skill == "reading" and test.type == "academic":
                    if raw_score == 0:
                        band_score = 0
                    elif raw_score == 1:
                        band_score = 1
                    elif raw_score >= 2 and raw_score <= 3:
                        band_score = 2
                    elif raw_score >= 4 and raw_score <= 5:
                        band_score = 2.5
                    elif raw_score >= 6 and raw_score <= 7:
                        band_score = 3
                    elif raw_score >= 8 and raw_score <= 9:
                        band_score = 3.5
                    elif raw_score >= 10 and raw_score <= 12:
                        band_score = 4
                    elif raw_score >= 13 and raw_score <= 14:
                        band_score = 4.5
                    elif raw_score >= 15 and raw_score <= 18:
                        band_score = 5
                    elif raw_score >= 19 and raw_score <= 22:
                        band_score = 5.5
                    elif raw_score >= 23 and raw_score <= 26:
                        band_score = 6
                    elif raw_score >= 27 and raw_score <= 29:
                        band_score = 6.5
                    elif raw_score >= 30 and raw_score <= 32:
                        band_score = 7
                    elif raw_score >= 33 and raw_score <= 34:
                        band_score = 7.5
                    elif raw_score >= 35 and raw_score <= 36:
                        band_score = 8
                    elif raw_score >= 37 and raw_score <= 38:
                        band_score = 8.5
                    else:
                        band_score = 9

                if test.skill == "reading" and test.type == "general":
                    if raw_score == 0:
                        band_score = 0
                    elif raw_score == 1:
                        band_score = 1
                    elif raw_score >= 2 and raw_score <= 5:
                        band_score = 2
                    elif raw_score >= 6 and raw_score <= 8:
                        band_score = 2.5
                    elif raw_score >= 9 and raw_score <= 11:
                        band_score = 3
                    elif raw_score >= 12 and raw_score <= 14:
                        band_score = 3.5
                    elif raw_score >= 15 and raw_score <= 18:
                        band_score = 4
                    elif raw_score >= 19 and raw_score <= 22:
                        band_score = 4.5
                    elif raw_score >= 23 and raw_score <= 26:
                        band_score = 5
                    elif raw_score >= 27 and raw_score <= 29:
                        band_score = 5.5
                    elif raw_score >= 30 and raw_score <= 31:
                        band_score = 6
                    elif raw_score >= 32 and raw_score <= 33:
                        band_score = 6.5
                    elif raw_score >= 34 and raw_score <= 35:
                        band_score = 7
                    elif raw_score == 36:
                        band_score = 7.5
                    elif raw_score >= 37 and raw_score <= 38:
                        band_score = 8
                    elif raw_score == 39:
                        band_score = 8.5
                    else:
                        band_score = 9
            except:
                return Response("Error in the test correction process.", status=status.HTTP_400_BAD_REQUEST)


            data = {'user_id':test.user.id,
                    'user_phone': test.user.phone_number,
                    'user_first_name': test.user.first_name,
                    'user_last_name': test.user.last_name,
                    'test_id':test.test_id,
                    'test_name': test.name,
                    'skill':test.skill,
                    'type':test.type,
                    'book': test.book.name,
                    'raw_score':raw_score,
                    'band_score':band_score,
                    'test_created_at':test.created_at}

            history = TestHistory()
            history.test = test
            history.user = test.user
            history.band_score = band_score
            history.raw_score = raw_score
            history.save()

            return Response(data, status=status.HTTP_200_OK)
        except:
            return Response("Test not found or something went wrong, try again", status=status.HTTP_400_BAD_REQUEST)






class UserWritingTests(GenericAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    serializer_class = WritingTestSerializer
    #queryset = Test.objects.all()
    #filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    #filterset_fields = ['user', 'created_at', 'skill', 'type']
    #search_fields = ['test_id', 'name']
    #ordering_fields = ['test_id', 'created_at', 'id']

    def get(self, *args, **kwargs):
        user_tests = WritingTest.objects.filter(user=self.request.user)
        tests = self.filter_queryset(user_tests)
        page = self.paginate_queryset(tests)
        if page is not None:
            serializer = WritingTestSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = WritingTestSerializer(tests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)






class UserSpeakingTests(GenericAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    serializer_class = SpeakingTestSerializer
    #queryset = Test.objects.all()
    #filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    #filterset_fields = ['user', 'created_at', 'skill', 'type']
    #search_fields = ['test_id', 'name']
    #ordering_fields = ['test_id', 'created_at', 'id']

    def get(self, *args, **kwargs):
        user_tests = SpeakingTest.objects.filter(user=self.request.user)
        tests = self.filter_queryset(user_tests)
        page = self.paginate_queryset(tests)
        if page is not None:
            serializer = SpeakingTestSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = SpeakingTestSerializer(tests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)









class CreateSpeaking(APIView):
    serializer_class = SpeakingCreateTestSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        req = self.request.data
        teacher = Teacher.objects.get(id=req['teacher'])
        req['amount'] = teacher.speaking_price
        req['user'] = self.request.user.id
        req['description'] = req['name']
        serializer = SpeakingCreateTestSerializer(data=req)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class CreateWriting(APIView):
    serializer_class = WritingCreateTestSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        req = self.request.data
        teacher = Teacher.objects.get(id=req['marker'])
        req['amount'] = teacher.writing_price
        req['user'] = self.request.user.id
        req['description'] = req['name']

        serializer = WritingCreateTestSerializer(data=req)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class AnswerWriting(APIView):
    serializer_class = WritingTestSerializer
    permission_classes = [IsAuthenticated]
    def patch(self, request, *args, **kwargs):
        test = WritingTest.objects.get(id=self.kwargs["id"])
        data = self.request.data
        data['marker'] = test.marker.id
        data['user'] = test.user.id
        data['type'] = test.type
        #data['skill'] = test.skill

        if self.request.user != test.user:
            return Response("You are not allowed to take this exam.",status=status.HTTP_406_NOT_ACCEPTABLE)

        if test.test_done == True:
            return Response("You are not allowed to change, the test is finished.",status=status.HTTP_406_NOT_ACCEPTABLE)

        delta = timezone.now() - test.created_at
        delta_time_minutes = delta.total_seconds() / 60

        if delta_time_minutes >= 360:
            return Response("Your exam time is over, Writing test time is 6 hours.",status=status.HTTP_406_NOT_ACCEPTABLE)


        serializer = self.serializer_class(test, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
