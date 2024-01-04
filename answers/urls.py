from django.urls import path
from answers.views import Answer

urlpatterns = [
    path("send", Answer.as_view(), name="send"),
]


