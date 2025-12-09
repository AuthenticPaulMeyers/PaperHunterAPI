from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required

# New chat session route
@login_required(login_url='users:login')
@api_view(['POST'])
def new_chat_session(request, paper_id):
    return Response({'message': 'New chat session created successfully!'}, status.HTTP_200_OK)

# List all of the authenticated user's past chat sessions
@login_required(login_url='users:login')
@api_view(['GET'])
def show_chats(request):
    # Placeholder
    chats = []

    return Response({'chats': chats}, status=status.HTTP_200_OK)

# Retrieve the message history for a specific chat session.
@login_required(login_url='users:login')
@api_view(['GET'])
def show_message_history(request, session_id):
    # Placeholder
    messages = []

    return Response({'messages': messages}, status=status.HTTP_200_OK)

# Send a user query to the AI tutor
@login_required(login_url='users:login')
@api_view(['POST'])
def user_query(request, session_id):
    # Placeholder
    response = []
    
    return Response({'response': response }, status=status.HTTP_200_OK)