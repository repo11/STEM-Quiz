from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
class Migration(migrations.Migration):
    initial=True
    dependencies=[migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations=[migrations.CreateModel(name='PerformanceReport',fields=[('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),('recommendations',models.JSONField(default=list)),('strong_topics',models.JSONField(default=list)),('weak_topics',models.JSONField(default=list)),('generated_at',models.DateTimeField(auto_now_add=True)),('student',models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name='reports',to=settings.AUTH_USER_MODEL))])]
