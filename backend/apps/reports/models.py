from django.conf import settings
from django.db import models
class PerformanceReport(models.Model):
    student=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='reports')
    recommendations=models.JSONField(default=list)
    strong_topics=models.JSONField(default=list)
    weak_topics=models.JSONField(default=list)
    generated_at=models.DateTimeField(auto_now_add=True)
