from django.urls import path
from teacher.views import TeacherList, TeacherItem, ReserveTimes

urlpatterns = [
    path("list", TeacherList.as_view(), name="list"),
    path('item/<int:id>', TeacherItem.as_view(), name='item'),
    path("reserve-times", ReserveTimes.as_view(), name="reserve-times"),
]


