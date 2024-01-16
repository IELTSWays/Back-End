from django.urls import path
from exam.views import AddQuestion, StartTest, Answer, StartTestNew, Report, UserTests


urlpatterns = [
    path("add-question", AddQuestion.as_view(), name="add-question"),
    path('test/<int:id>', AddQuestion.as_view(), name='test'),
    path('start', StartTest.as_view(), name='start'),
    path('answer/<str:id>', Answer.as_view(), name='answer'),
    path('start-test', StartTestNew.as_view(), name='start-test'),
    path('report/<str:id>', Report.as_view(), name='report'),
    path('user-tests', UserTests.as_view(), name='user-tests'),
]


