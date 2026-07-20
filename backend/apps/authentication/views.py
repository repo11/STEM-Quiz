from django.contrib.auth import login, logout
from django.middleware.csrf import get_token
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LoginSerializer, RegisterSerializer, UserSerializer
class CsrfView(APIView):
    permission_classes=[permissions.AllowAny]
    def get(self, request): return Response({'csrfToken': get_token(request)})
class RegisterView(APIView):
    permission_classes=[permissions.AllowAny]
    def post(self, request):
        s=RegisterSerializer(data=request.data); s.is_valid(raise_exception=True); user=s.save(); login(request,user); return Response(UserSerializer(user).data,status=201)
class LoginView(APIView):
    permission_classes=[permissions.AllowAny]
    def post(self, request):
        s=LoginSerializer(data=request.data); s.is_valid(raise_exception=True); login(request,s.validated_data['user']); return Response(UserSerializer(s.validated_data['user']).data)
class LogoutView(APIView):
    def post(self, request): logout(request); return Response(status=204)
class MeView(APIView):
    def get(self, request): return Response(UserSerializer(request.user).data)
    def patch(self, request):
        s=UserSerializer(request.user,data=request.data,partial=True); s.is_valid(raise_exception=True); s.save(); return Response(s.data)
