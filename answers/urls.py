from django.urls import path
from answers.views import Answer, CorrectAnswer

urlpatterns = [
    path("add-correct-answer", Answer.as_view(), name="add-correct-answer"),
    path("correct-answer/<str:name>", CorrectAnswer.as_view(), name="correct-answer"),
]


