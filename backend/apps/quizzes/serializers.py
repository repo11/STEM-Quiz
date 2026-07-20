from rest_framework import serializers
from .models import Question, Quiz, QuizAttempt
class QuestionSerializer(serializers.ModelSerializer):
    class Meta: model=Question; fields='__all__'
    def validate(self,data):
        q=Question(**data); q.clean(); return data
class QuizSerializer(serializers.ModelSerializer):
    questions=QuestionSerializer(many=True, read_only=True)
    question_ids=serializers.PrimaryKeyRelatedField(queryset=Question.objects.all(), many=True, write_only=True, source='questions')
    class Meta: model=Quiz; fields=['id','title','subject','duration','questions','question_ids','created_at']
    def validate(self,data):
        if data.get('duration',1) <= 0: raise serializers.ValidationError({'duration':'Duration must be greater than zero.'})
        if not data.get('questions'): raise serializers.ValidationError({'questions':'Quiz must contain at least one question.'})
        return data
class AttemptSerializer(serializers.ModelSerializer):
    class Meta: model=QuizAttempt; fields='__all__'; read_only_fields=['student','score','percentage','completed_at']
class SubmitQuizSerializer(serializers.Serializer):
    answers=serializers.DictField(child=serializers.CharField(allow_blank=False)); time_taken=serializers.IntegerField(min_value=0)
