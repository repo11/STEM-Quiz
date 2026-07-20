from rest_framework import serializers
from .models import PerformanceReport
class PerformanceReportSerializer(serializers.ModelSerializer):
    class Meta: model=PerformanceReport; fields='__all__'; read_only_fields=['student','generated_at']
