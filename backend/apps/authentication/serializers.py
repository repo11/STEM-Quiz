import re
from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User

PASSWORD_RE=re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$')
NAME_RE=re.compile(r'^[A-Za-z\s-]+$')
class UserSerializer(serializers.ModelSerializer):
    class Meta: model=User; fields=['id','first_name','last_name','email','student_id','role','created_at']
class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True); confirm_password=serializers.CharField(write_only=True)
    class Meta: model=User; fields=['first_name','last_name','email','student_id','password','confirm_password']
    def validate_first_name(self,v):
        if not v or not NAME_RE.match(v): raise serializers.ValidationError('First name must contain alphabetic characters only.'); return v
    def validate_last_name(self,v):
        if not v or not NAME_RE.match(v): raise serializers.ValidationError('Last name must contain alphabetic characters only.'); return v
    def validate_password(self,v):
        if not PASSWORD_RE.match(v): raise serializers.ValidationError('Password needs 8 characters, upper/lowercase, number, and special character.'); return v
    def validate(self,data):
        if data['password'] != data['confirm_password']: raise serializers.ValidationError({'confirm_password':'Passwords must match.'})
        return data
    def create(self,data):
        data.pop('confirm_password'); return User.objects.create_user(role=User.Role.STUDENT, **data)
class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField(); password=serializers.CharField()
    def validate(self,data):
        user=authenticate(email=data['email'], password=data['password'])
        if not user: raise serializers.ValidationError('Invalid email or password.')
        data['user']=user; return data
