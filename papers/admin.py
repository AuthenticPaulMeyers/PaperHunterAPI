from django.contrib import admin
from .models import Paper, Level, Subject, DownloadRecord

class DownloadRecordAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user__username', 'paper__subject__name', 'paper__year', 'paper__paper_number', 'downloaded_at']
    search_fields = ['paper__title', 'user__username']

class PaperAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'level__name', 'subject__name', 'year', 'paper_number', 'uploaded_at']
    list_filter = ['level']
    search_fields = ['title', 'level__name']

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

# Register your models here.
admin.site.register(Level)
admin.site.register(Subject)
admin.site.register(Paper, PaperAdmin)
admin.site.register(DownloadRecord, DownloadRecordAdmin)