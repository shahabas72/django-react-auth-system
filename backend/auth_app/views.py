from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate

# Create your views here.

# User Registration
@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=400)
    
    user = User.objects.create_user(username=username, password=password)
    token, _ = Token.objects.get_or_create(user=user)
    
    return Response({'token': token.key, 'message': 'User registered successfully'})

# User Login
@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)
    
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'message': 'Login successful'})
    
    return Response({'error': 'Invalid credentials'}, status=400)

# User Logout
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    request.auth.delete()  # Deletes the authentication token
    return Response({'message': 'Logout successful'})

# Protected Dashboard Route
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    return Response({'message': f'Welcome {request.user.username}, this is your dashboard'})
