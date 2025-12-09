from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

# Register route
@api_view(['POST'])
def register(request):
      return Response({'message': 'User registration endpoint'})

# Login route
@api_view(['POST'])
def login(request):
        return Response({'message': 'User login endpoint'})

# Logout route
@api_view(['POST'])
def logout(request):
        return Response({'message': 'User logout endpoint'})

# Profile route
@api_view(['GET'])
def profile(request):
        return Response({'message': 'User profile endpoint'})

# Update profile route
@api_view(['PUT'])
def update_profile(request):
        return Response({'message': 'Update user profile endpoint'})

# Change password route
@api_view(['PUT'])
def change_password(request):
        return Response({'message': 'Change user password endpoint'})


