from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
@admin.register(User)
class STEMUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'student_id', 'role', 'is_staff', 'created_at')
    ordering = ('email',)
    fieldsets = UserAdmin.fieldsets + (('STEM Profile', {'fields': ('student_id', 'role', 'avatar')}),)
    add_fieldsets = UserAdmin.add_fieldsets + (('STEM Profile', {'fields': ('email', 'student_id', 'role')}),)
