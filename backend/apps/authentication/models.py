from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models

class UserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self, email, password=None, **extra):
        if not email: raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra)
        user.set_password(password); user.save(using=self._db); return user
    def create_superuser(self, email, password=None, **extra):
        extra.setdefault('is_staff', True); extra.setdefault('is_superuser', True); extra.setdefault('role', User.Role.ADMIN)
        return self.create_user(email, password, **extra)

class User(AbstractUser):
    class Role(models.TextChoices): STUDENT='student','Student'; ADMIN='admin','Administrator'
    username = models.CharField(max_length=150, blank=True)
    email = models.EmailField(unique=True)
    student_id = models.CharField(max_length=40, unique=True, null=True, blank=True)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.STUDENT)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD='email'; REQUIRED_FIELDS=[]; objects=UserManager()
    class Meta: indexes=[models.Index(fields=['email']), models.Index(fields=['student_id'])]
    def __str__(self): return self.email
