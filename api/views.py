from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import HoustonUser
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import authenticate
import json

@api_view(['GET'])
def index(request):
    return Response({'message': 'Hello, world!'})

@csrf_exempt
@api_view(['POST'])
def register(request):
    try:
        data = json.loads(request.body)
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')
        # You may add additional fields such as email, first_name, last_name, etc.
        if email and password:
            user = HoustonUser.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=email, password=password)
            return JsonResponse({'message': 'User registered successfully'}, status=201)
        else:
            return JsonResponse({'error': 'Email and Password are required'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@api_view(['POST'])
def login(request):
    try:
        # Get username and password from request data
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        # Perform authentication (You can use Django's built-in authentication system or custom authentication logic)
        user_authenticated = authenticate(request, username=email, password=password)

        if user_authenticated:
            # Return success message
            return JsonResponse({'message': 'Login successful'})
        else:
            # Return error message
            return JsonResponse({'error': 'Invalid username or password'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
