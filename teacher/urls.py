from django.urls import path
from teacher.views import TeacherList, TeacherItem, ReserveTimes, TeacherReserveTimes, TeacherTimes, TeacherProfile

urlpatterns = [
    path("list", TeacherList.as_view(), name="list"),
    path('item/<int:id>', TeacherItem.as_view(), name='item'),
    path("reserve-times", ReserveTimes.as_view(), name="reserve-times"),
    path("teachers-reserve-times", TeacherReserveTimes.as_view(), name="teachers-reserve-times"),
    path("teacher-times", TeacherTimes.as_view(), name="teacher-times"),
    path("profile", TeacherProfile.as_view(), name="profile"),
]


