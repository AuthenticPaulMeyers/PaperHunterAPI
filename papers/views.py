from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import Paper, Level, Subject, DownloadRecord
from .serializers import PaperSerializer, LevelSerializer, SubjectSerializer, DownloadRecordSerializer
from .utils.filters import PaperFilter
from rest_framework.views import APIView

# Home page route
class IndexView(APIView):

    permission_classes=[AllowAny]
    def get(self, request, *args, **kwargs):
        # Functionalities in this route:
        # Done: Filter by Level: /api/papers/?level=MSCE
        # Done: Filter by Level & Subject: /api/papers/?level=MSCE&subject=Mathematics
        # Done: Search by Keyword: /api/papers/?search=English
        # Todo: We should implement pagination for large datasets(to be implemented later).
        try:
            papers_queryset = Paper.objects.all().order_by('year')
            paper_filter = PaperFilter(request.GET, queryset=papers_queryset)
            filtered_papers = paper_filter.qs
            papers_count = filtered_papers.count()
            serializer = PaperSerializer(filtered_papers, many=True)
            papers = serializer.data

            if not papers:
                return Response({'message': 'No papers found matching the criteria.'}, status=status.HTTP_404_NOT_FOUND)
            return Response({'papers': papers, 'papers_count': papers_count}, status=status.HTTP_200_OK)
        
        except Paper.DoesNotExist:
            return Response({'error': 'Papers not found.'}, status=status.HTTP_404_NOT_FOUND)

# Read paper route
class ReadPaperView(APIView):

    permission_classes=[AllowAny]
    def get(self, request, paper_id, *args, **kwargs):
        try:
            paper = Paper.objects.get(id=paper_id)
            serializer = PaperSerializer(paper)
            return Response({'paper': serializer.data}, status=status.HTTP_200_OK)
        
        except Paper.DoesNotExist:
            return Response({'error': 'Paper not found.'}, status=status.HTTP_404_NOT_FOUND)

# List all examination levels route
class ListExamLevelsView(APIView):

    permission_classes=[AllowAny]
    def get(self, request, *args, **kwargs):
        try:
            levels = Level.objects.all()
            serializer = LevelSerializer(levels, many=True)
            return Response({'examination_levels': serializer.data}, status=status.HTTP_200_OK)
        except Level.DoesNotExist:
            return Response({'error': 'Level not found.'}, status=status.HTTP_404_NOT_FOUND)
        

# List all subjects route
class ListSubjectsView(APIView):
    
    permission_classes=[AllowAny]
    def get(self, request, *args, **kwargs):
        try:
            subjects = Subject.objects.all()
            serializer = SubjectSerializer(subjects, many=True)
            return Response({'subjects': serializer.data}, status=status.HTTP_200_OK)
        
        except Subject.DoesNotExist:
            return Response({'error': 'Subject not found.'}, status=status.HTTP_404_NOT_FOUND)
        

# Download paper route  
class DownloadPaperView(APIView):

    permission_classes=[IsAuthenticated]
    def get(self, request, paper_id, *args, **kwargs):
        user = request.user

        try:
            paper = Paper.objects.get(id=paper_id)
            # Will implement proper download logic here later
            print("DOWNLOAD:", paper.file)
            download = DownloadRecord.objects.create(paper=paper, user=user)
            download.save()
            return Response({'message': 'Paper downloaded successfully!'}, status=status.HTTP_200_OK)

        except Paper.DoesNotExist:
            return Response({'error': 'Paper not found.'}, status=status.HTTP_404_NOT_FOUND)

# Show downloaded papers
class ShowDownloadsView(APIView):

    permission_classes=[IsAuthenticated]
    def get(self, request, *args, **kwargs):
        user = request.user

        try:
            downloads = DownloadRecord.objects.filter(user=user)
            if not downloads:
                return Response({'message': 'You do not have downloaded files.'}, status=status.HTTP_404_NOT_FOUND)
            
            download_serializer = DownloadRecordSerializer(downloads, many=True)

            return Response({'downloads': download_serializer.data}, status=status.HTTP_200_OK)
        
        except DownloadRecord.DoesNotExist:
            return Response({'error': 'Download records not found.'}, status=status.HTTP_404_NOT_FOUND)

    