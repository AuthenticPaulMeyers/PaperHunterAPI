from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Custom User admin configuration"""
    list_display = ['username', 'email', 'first_name', 'last_name', 'grade_level', 'school_name', 'is_staff']
    list_filter = ['grade_level', 'is_staff', 'is_active', 'date_joined']
    search_fields = ['username', 'email', 'first_name', 'last_name', 'school_name']
    
    # Add custom fields to the fieldsets
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Student Information', {
            'fields': ('school_name', 'grade_level', 'profile_picture', 'preferences')
        }),
    )
    
    # Add custom fields to add_fieldsets
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Student Information', {
            'fields': ('school_name', 'grade_level')
        }),
    )

