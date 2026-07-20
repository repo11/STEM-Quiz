from django.db.models import Count
from rest_framework import viewsets, permissions
from .models import Subject
from .serializers import SubjectSerializer
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self,request,view): return request.method in permissions.SAFE_METHODS or (request.user.is_authenticated and request.user.is_staff)
class SubjectViewSet(viewsets.ModelViewSet):
    queryset=Subject.objects.annotate(quiz_count=Count('quizzes'))
    serializer_class=SubjectSerializer; permission_classes=[IsAdminOrReadOnly]
    search_fields=['name','description']; ordering_fields=['name','created_at']
