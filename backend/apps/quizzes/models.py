from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from apps.subjects.models import Subject

class Question(models.Model):
    class Type(models.TextChoices): MULTIPLE_CHOICE='multiple_choice','Multiple Choice'; TRUE_FALSE='true_false','True / False'; NUMERIC='numeric','Numeric'
    class Difficulty(models.TextChoices): EASY='easy','Easy'; MEDIUM='medium','Medium'; HARD='hard','Hard'
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='questions')
    question_type=models.CharField(max_length=30,choices=Type.choices)
    question_text=models.TextField()
    options=models.JSONField(default=list, blank=True)
    answer=models.CharField(max_length=255)
    explanation=models.TextField()
    difficulty=models.CharField(max_length=20,choices=Difficulty.choices)
    tolerance=models.DecimalField(max_digits=8, decimal_places=4, default=0)
    def clean(self):
        if self.question_type == self.Type.MULTIPLE_CHOICE:
            if len(self.options) < 4: raise ValidationError('Multiple choice questions need at least four options.')
            if len(set(self.options)) != len(self.options): raise ValidationError('Options cannot be duplicated.')
            if self.answer not in self.options: raise ValidationError('Correct answer must be one of the options.')
        if self.question_type == self.Type.TRUE_FALSE and self.answer.lower() not in ['true','false']:
            raise ValidationError('True / False answers must be True or False.')
        if self.question_type == self.Type.NUMERIC: float(self.answer)
    def check_answer(self, value):
        if self.question_type == self.Type.NUMERIC: return abs(float(value)-float(self.answer)) <= float(self.tolerance)
        return str(value).strip().lower() == self.answer.strip().lower()

class Quiz(models.Model):
    title=models.CharField(max_length=160)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='quizzes')
    duration=models.PositiveIntegerField(help_text='Duration in minutes')
    questions=models.ManyToManyField(Question, related_name='quizzes')
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta: unique_together=('title','subject'); ordering=['subject','title']
    def clean(self):
        if self.duration <= 0: raise ValidationError('Duration must be greater than zero.')

class QuizAttempt(models.Model):
    student=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='attempts')
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name='attempts')
    answers=models.JSONField(default=dict)
    score=models.PositiveIntegerField(default=0)
    percentage=models.DecimalField(max_digits=5,decimal_places=2,default=0)
    time_taken=models.PositiveIntegerField(default=0)
    completed_at=models.DateTimeField(auto_now_add=True)
    class Meta: unique_together=('student','quiz'); ordering=['-completed_at']
    @property
    def status(self): return 'Passed' if self.percentage >= 70 else 'Needs Practice'
