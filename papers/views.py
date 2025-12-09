from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required

# Home page route
# We should not forget to add the following functionalities in this route:
# ●	Filter by Level: /api/papers/?level=MSCE
# ●	Filter by Level & Subject: /api/papers/?level=MSCE&subject=Mathematics
# ●	Search by Keyword: /api/papers/?search=English
# ● We should implement pagination for large datasets.
@api_view(['GET'])
def index(request):
    # Placeholder
    papers = []

    return Response({'papers': papers}, status=status.HTTP_200_OK)

# Read papers route
@api_view(['GET'])
def read_paper(request, paper_id):
    
    return Response({'message': 'You are reading a Mathematics paper!'})

# List all examination levels route
@api_view(['GET'])
def examination_levels(request):
    # Placeholder
    levels = []

    return Response({'examination_levels': levels}, status=status.HTTP_200_OK)

# List all subjects route
@api_view(['GET'])
def subjects(request):
    # Placeholder
    subjects = []

    return Response({'subjects': subjects}, status=status.HTTP_200_OK)

# List paper stats route
@api_view(['GET'])
def paper_stats(request):
    # Placeholder
    stats = {}

    return Response({'paper_stats': stats}, status=status.HTTP_200_OK)

# Download paper route
@login_required(login_url='users:login')
@api_view(['GET'])
def download_paper(request, paper_id):
    return Response({'message': 'Paper downloaded successfully!'}, status.HTTP_200_OK)

# Show downloaded papers
@login_required(login_url='users:login')
@api_view(['GET'])
def show_downloads(request):
    # Placeholder
    downloads = []

    return Response({'downloads': downloads}, status=status.HTTP_200_OK)