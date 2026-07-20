from django.db import models
class Subject(models.Model):
    name=models.CharField(max_length=120, unique=True)
    description=models.TextField()
    image_url=models.URLField(blank=True)
    difficulty=models.CharField(max_length=30, default='Beginner')
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta: ordering=['name']
    def __str__(self): return self.name
