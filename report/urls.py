from django.urls import path
from report.views import FullReport, MediaReport

urlpatterns = [
    path('full-report/<str:id>', FullReport.as_view(), name='full-report'),
    path('media-report/<str:id>', MediaReport.as_view(), name='media-report'),
]


