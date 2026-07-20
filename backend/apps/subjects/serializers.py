from rest_framework import serializers
from .models import Subject
class SubjectSerializer(serializers.ModelSerializer):
    quiz_count=serializers.IntegerField(read_only=True, default=0)
    class Meta: model=Subject; fields='__all__'
    def validate_name(self,v):
        if not v.strip(): raise serializers.ValidationError('Subject name is required.'); return v.strip()
    def validate_description(self,v):
        if not v.strip(): raise serializers.ValidationError('Description cannot be empty.'); return v
