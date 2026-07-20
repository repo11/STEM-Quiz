from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Question, Quiz, QuizAttempt
from .serializers import AttemptSerializer, QuestionSerializer, QuizSerializer, SubmitQuizSerializer
class AdminWrite(permissions.BasePermission):
    def has_permission(self,request,view): return request.method in permissions.SAFE_METHODS or request.user.is_staff
class QuestionViewSet(viewsets.ModelViewSet): queryset=Question.objects.all(); serializer_class=QuestionSerializer; permission_classes=[AdminWrite]
class QuizViewSet(viewsets.ModelViewSet):
    queryset=Quiz.objects.prefetch_related('questions').select_related('subject'); serializer_class=QuizSerializer; permission_classes=[AdminWrite]
    @action(detail=True, methods=['post'])
    def submit(self, request, pk=None):
        quiz=self.get_object()
        if QuizAttempt.objects.filter(student=request.user, quiz=quiz).exists(): return Response({'detail':'Quiz already submitted.'}, status=400)
        s=SubmitQuizSerializer(data=request.data); s.is_valid(raise_exception=True)
        answers=s.validated_data['answers']; score=0; feedback=[]; questions=list(quiz.questions.all())
        if not questions: return Response({'detail':'This quiz has no questions.'}, status=400)
        for q in questions:
            given=answers.get(str(q.id),''); correct=q.check_answer(given)
            score += int(correct); feedback.append({'question':q.id,'isCorrect':correct,'correctAnswer':q.answer,'explanation':q.explanation})
        pct=round(score/len(questions)*100,2)
        attempt=QuizAttempt.objects.create(student=request.user, quiz=quiz, answers=answers, score=score, percentage=pct, time_taken=s.validated_data['time_taken'])
        return Response({'attempt':AttemptSerializer(attempt).data,'feedback':feedback})
class AttemptViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class=AttemptSerializer
    def get_queryset(self): return QuizAttempt.objects.all() if self.request.user.is_staff else self.request.user.attempts.all()
