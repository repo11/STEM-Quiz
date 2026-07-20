from django.db import migrations, models
class Migration(migrations.Migration):
    initial=True
    dependencies=[]
    operations=[migrations.CreateModel(name='Subject', fields=[('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),('name',models.CharField(max_length=120,unique=True)),('description',models.TextField()),('image_url',models.URLField(blank=True)),('difficulty',models.CharField(default='Beginner',max_length=30)),('created_at',models.DateTimeField(auto_now_add=True))], options={'ordering':['name']})]
