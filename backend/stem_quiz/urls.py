from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('apps.authentication.urls')),
    path('api/students/', include('apps.students.urls')),
    path('api/subjects/', include('apps.subjects.urls')),
    path('api/quizzes/', include('apps.quizzes.urls')),
    path('api/reports/', include('apps.reports.urls')),
    path('api/dashboard/', include('apps.dashboard.urls')),
    re_path(r'^(?!api/|admin/|static/).*$', TemplateView.as_view(template_name='index.html'), name='spa'),
]
