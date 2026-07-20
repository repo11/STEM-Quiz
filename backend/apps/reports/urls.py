from django.urls import path
from .views import ExportCsvView, ReportView
urlpatterns=[path('',ReportView.as_view()),path('export/csv/',ExportCsvView.as_view())]
