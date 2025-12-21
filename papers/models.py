from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Level(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Subjects
class Subject(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# Papers
class Paper(models.Model):
    title = models.CharField(max_length=200)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    paper_number = models.CharField(max_length=20)
    file = models.FileField(upload_to='papers/')
    downloads = models.PositiveIntegerField(default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_indexed = models.BooleanField(default=False)

    def __str__(self):
        return self.subject.name

class DownloadRecord(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    downloaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.paper.title