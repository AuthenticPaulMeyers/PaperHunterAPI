from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator


class User(AbstractUser):
    """
    Extended User model with additional fields for student information
    """
    GRADE_LEVEL_CHOICES = [
        ('JCE', 'Junior Certificate of Education'),
        ('MSCE', 'Malawi School Certificate of Education'),
    ]
    
    # Additional profile fields
    school_name = models.CharField(max_length=200, blank=True, null=True)
    grade_level = models.CharField(
        max_length=10, 
        choices=GRADE_LEVEL_CHOICES, 
        blank=True, 
        null=True
    )
    profile_picture = models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]
    )
    preferences = models.JSONField(
        default=dict,
        blank=True,
        help_text='User preferences like theme, notifications, etc.'
    )
    
    # Override email to make it required and unique
    email = models.EmailField(unique=True)
    
    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return self.username
    
    @property
    def full_name(self):
        """Return user's full name"""
        return f"{self.first_name} {self.last_name}".strip() or self.username
