from django.db.models import Avg, Count, Max, Min
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.authentication.models import User
from apps.subjects.models import Subject
from apps.quizzes.models import Question, Quiz, QuizAttempt
class DashboardView(APIView):
    def get(self, request):
        attempts = QuizAttempt.objects.all() if request.user.is_staff else request.user.attempts.all()
        stats=attempts.aggregate(total_quizzes=Count('id'),highest_score=Max('percentage'),lowest_score=Min('percentage'),average_score=Avg('percentage'))
        return Response({'stats':stats,'total_subjects':Subject.objects.count(),'weekly_progress':[],'subject_performance':[],'recent_activity':[]})
class AdminAnalyticsView(APIView):
    def get(self, request):
        if not request.user.is_staff: return Response({'detail':'Access denied.'}, status=403)
        return Response({'total_students':User.objects.filter(role='student').count(),'total_subjects':Subject.objects.count(),'total_quizzes':Quiz.objects.count(),'total_questions':Question.objects.count(),'average_scores':QuizAttempt.objects.aggregate(avg=Avg('percentage'))['avg'] or 0})
