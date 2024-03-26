from django.urls import path
from report.views import FullReport, MediaReport, FullReportPayment, FullReportVerify, MediaReportPayment, MediaReportVerify

urlpatterns = [
    path('full-report/<str:id>', FullReport.as_view(), name='full-report'),
    path('full-report-payment/<str:id>', FullReportPayment.as_view(), name='full-report-payment'),
    path('full-report-verify/<str:id>/', FullReportVerify.as_view(), name='full-report-verify'),
    path('media-report/<str:id>', MediaReport.as_view(), name='media-report'),
    path('media-report-payment/<str:id>', MediaReportPayment.as_view(), name='media-report-payment'),
    path('media-report-verify/<str:id>/', MediaReportVerify.as_view(), name='media-report-verify'),
]


