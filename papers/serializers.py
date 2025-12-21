from rest_framework import serializers
from .models import Paper, Level, Subject, DownloadRecord

# Serializer for Level model
class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['name']

# Serializer for Subject model
class SubjectSerializer(serializers.ModelSerializer):
      class Meta:
            model = Subject
            fields = ['name']

# Serializer for Paper model
class PaperSerializer(serializers.ModelSerializer):
      level = LevelSerializer(read_only=True)
      subject = SubjectSerializer(read_only=True)

      class Meta:
          model = Paper
          fields = '__all__'

# Serializer for DownloadRecord model
class DownloadRecordSerializer(serializers.ModelSerializer):
      paper = PaperSerializer(read_only=True)
      class Meta:
          model = DownloadRecord
          fields = '__all__'
