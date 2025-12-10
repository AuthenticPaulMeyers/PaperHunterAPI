from django.db import models

# Levels
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
      year = models.CharField(max_length=4)
      paper_number = models.CharField(max_length=20)
      file_link = models.TextField()
      uploaded_at = models.DateTimeField(auto_now_add=True)
      is_indexed = models.BooleanField(default=False)

      def __str__(self):
          return f"{self.title} - {self.subject.name} ({self.year})"
      