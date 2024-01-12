from exam.models import Test
from exam.serializers import QuestionSerializer, TestSerializer, AnswerSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from answers.models import TestCorrectAnswer



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

        data['answers'] = {}

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
            return Response(data, status=status.HTTP_200_OK)
        except:
            return Response("Test not found or something went wrong, try again", status=status.HTTP_400_BAD_REQUEST)

