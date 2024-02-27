from django.urls import path
from report.views import FullReport

urlpatterns = [
    path('full-report/<str:id>', FullReport.as_view(), name='full-report'),
]


