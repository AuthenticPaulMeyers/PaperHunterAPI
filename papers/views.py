from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from .models import Paper, Level, Subject
from .serializers import PaperSerializer, LevelSerializer, SubjectSerializer
from .utils.filters import PaperFilter

# Home page route
@api_view(['GET'])
def index(request):
    # We should add the following functionalities in this route:
    # Done: Filter by Level: /api/papers/?level=MSCE
    # Done:Filter by Level & Subject: /api/papers/?level=MSCE&subject=Mathematics
    # Done:Search by Keyword: /api/papers/?search=English
    # We should implement pagination for large datasets(to be implemented later).

    try:
        papers_queryset = Paper.objects.all().order_by('year')
        paper_filter = PaperFilter(request.GET, queryset=papers_queryset)
        filtered_papers = paper_filter.qs
        papers_count = filtered_papers.count()
        serializer = PaperSerializer(filtered_papers, many=True)
        papers = serializer.data

        if not papers:
            return Response({'message': 'No papers found matching the criteria.'}, status=status.HTTP_404_NOT_FOUND)
    
    except Paper.DoesNotExist:
        return Response({'error': 'Papers not found.'}, status=status.HTTP_404_NOT_FOUND)

    return Response({'papers': papers, 'papers_count': papers_count}, status=status.HTTP_200_OK)

# Read paper route
@api_view(['GET'])
def read_paper(request, paper_id):
    try:
        paper = Paper.objects.get(id=paper_id)
    except Paper.DoesNotExist:
        return Response({'error': 'Paper not found.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = PaperSerializer(paper)
    return Response({'paper': serializer.data}, status=status.HTTP_200_OK)

# List all examination levels route
@api_view(['GET'])
def examination_levels(request):
    try:
        levels = Level.objects.all()
    except Level.DoesNotExist:
        return Response({'error': 'Level not found.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = LevelSerializer(levels, many=True)

    return Response({'examination_levels': serializer.data}, status=status.HTTP_200_OK)

# List all subjects route
@api_view(['GET'])
def subjects(request):
    try:
        subjects = Subject.objects.all()
    except Subject.DoesNotExist:
        return Response({'error': 'Subject not found.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = SubjectSerializer(subjects, many=True)

    return Response({'subjects': serializer.data}, status=status.HTTP_200_OK)

# Download paper route
@login_required(login_url='users:login')
@api_view(['GET'])
def download_paper(request, paper_id):
    # To be edited later. I have just copied the code from the read papers route
    try:
        paper = Paper.objects.get(id=paper_id)
    except Paper.DoesNotExist:
        return Response({'error': 'Paper not found.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = PaperSerializer(paper)
    return Response({'paper': serializer.data, 'message': 'Paper downloaded successfully!'}, status=status.HTTP_200_OK)

# Show downloaded papers
@login_required(login_url='users:login')
@api_view(['GET'])
def show_downloads(request):
    # Placeholder
    downloads = []

    return Response({'downloads': downloads}, status=status.HTTP_200_OK)

# Upload papers
@login_required(login_url='users:login')
@api_view(['POST'])
def upload_papers(request):
    # get paper infor
    # data = request.POST
    # title = data.title
    # year
    # level
    # subject
    # paper_number
    # file
    ...