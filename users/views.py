from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Register route
@api_view(['POST'])
def register(request):
      return Response({'message': 'User registration endpoint'}, status=status.HTTP_201_CREATED)

# Login route
@api_view(['POST'])
def login(request):
        return Response({'message': 'User login endpoint'}, status=status.HTTP_200_OK)

# Logout route
@api_view(['POST'])
def logout(request):
        return Response({'message': 'User logout endpoint'}, status=status.HTTP_200_OK)

# Profile route
@api_view(['GET'])
def profile(request):
        return Response({'message': 'User profile endpoint'}, status=status.HTTP_200_OK)

# Update profile route
@api_view(['PUT'])
def update_profile(request):
        return Response({'message': 'Update user profile endpoint'}, status=status.HTTP_200_OK)

# Change password route
@api_view(['PUT'])
def change_password(request):
        return Response({'message': 'Change user password endpoint'}, status=status.HTTP_200_OK)


