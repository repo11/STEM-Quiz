from django.urls import path
from .views import AdminAnalyticsView, DashboardView
urlpatterns=[path('',DashboardView.as_view()),path('admin/',AdminAnalyticsView.as_view())]
