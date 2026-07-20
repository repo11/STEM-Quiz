from rest_framework import permissions, viewsets
from apps.authentication.models import User
from apps.authentication.serializers import UserSerializer
class AdminOnly(permissions.BasePermission):
    def has_permission(self,request,view): return request.user.is_staff
class StudentViewSet(viewsets.ModelViewSet):
    queryset=User.objects.filter(role='student'); serializer_class=UserSerializer; permission_classes=[AdminOnly]
    search_fields=['first_name','last_name','email','student_id']; ordering_fields=['created_at','email']
