from django.urls import path
from exam.views import AddQuestion

urlpatterns = [
    path("add-question", AddQuestion.as_view(), name="add-question"),
    path('test/<int:id>', AddQuestion.as_view(), name='test'),
]


