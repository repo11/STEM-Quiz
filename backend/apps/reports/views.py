from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PerformanceReport
from .serializers import PerformanceReportSerializer
class ReportView(APIView):
    def get(self, request):
        attempts=request.user.attempts.select_related('quiz__subject')
        if not attempts.exists(): return Response({'detail':'Complete at least one quiz before generating reports.'}, status=400)
        weak=[]; strong=[]
        for a in attempts:
            (strong if a.percentage>=80 else weak).append(a.quiz.subject.name)
        rec=[f'Review {t}' for t in sorted(set(weak))] or ['Keep practicing advanced STEM challenges']
        report=PerformanceReport.objects.create(student=request.user,recommendations=rec,strong_topics=list(set(strong)),weak_topics=list(set(weak)))
        return Response(PerformanceReportSerializer(report).data)
class ExportCsvView(APIView):
    def get(self, request):
        resp=HttpResponse(content_type='text/csv'); resp['Content-Disposition']='attachment; filename="score-history.csv"'; resp.write('Date,Subject,Quiz,Score,Percentage,Time Taken,Status\n')
        for a in request.user.attempts.select_related('quiz__subject'): resp.write(f'{a.completed_at},{a.quiz.subject.name},{a.quiz.title},{a.score},{a.percentage},{a.time_taken},{a.status}\n')
        return resp
