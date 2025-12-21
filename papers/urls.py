
from django.urls import path
from .views import ShowDownloadsView, ListSubjectsView, ListExamLevelsView, IndexView, ReadPaperView, DownloadPaperView

# Create URL patterns here.
app_name = 'papers'     
urlpatterns = [
      path('', IndexView.as_view(), name='index'),
      path('read/<int:paper_id>/', ReadPaperView.as_view(), name='read_paper'),
      path('levels/', ListExamLevelsView.as_view(), name='examination_levels'),
      path('subjects/', ListSubjectsView.as_view(), name='subjects'),
      path('<int:paper_id>/download/', DownloadPaperView.as_view(), name='download_paper'),
      path('downloads/', ShowDownloadsView.as_view(), name='show_downloads'),
      
]