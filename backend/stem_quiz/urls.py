from django.contrib import admin
from django.urls import include, path
urlpatterns = [path('admin/', admin.site.urls), path('api/auth/', include('apps.authentication.urls')), path('api/students/', include('apps.students.urls')), path('api/subjects/', include('apps.subjects.urls')), path('api/quizzes/', include('apps.quizzes.urls')), path('api/reports/', include('apps.reports.urls')), path('api/dashboard/', include('apps.dashboard.urls'))]
