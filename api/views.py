from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.models import HoustonUser
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import authenticate
from .serializers import HoustonUserSerializer
import json

@api_view(["GET"])
def index(request):
    return Response({"message": "Hello, world!"})


@csrf_exempt
@api_view(["POST"])
def register(request):
    response = {
        "status": status.HTTP_200_OK,
        "data": {},
        "error": [],
    }
    try:
        data = json.loads(request.body)
        first_name = data.get("firstName")
        last_name = data.get("lastName")
        email = data.get("email")
        password = data.get("password")
        # You may add additional fields such as email, first_name, last_name, etc.
        if email and password:
            # Check if username (email) already exists
            if HoustonUser.objects.filter(username=email).exists():
                response["status"] = status.HTTP_400_BAD_REQUEST
                response["error"] = ["Email already exists"]
            else:
                user = HoustonUser.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    username=email,
                    password=password,
                )
                response["data"] = {"message": "User registered successfully"}
                response["status"] = status.HTTP_201_CREATED
        else:
            response["status"] = status.HTTP_400_BAD_REQUEST
            response["error"] = ["Email and Password are required"]
    except Exception as e:
        response["status"] = status.HTTP_500_INTERNAL_SERVER_ERROR
        response["error"] = [str(e)]

    return JsonResponse(response, status=response["status"])


@api_view(["POST"])
def login(request):
    try:
        # Get username and password from request data
        data = json.loads(request.body)
        email = data.get("email")
        password = data.get("password")

        # Perform authentication
        user = authenticate(request, username=email, password=password)
        response = {"data": {}, "error": []}
        res_status = status.HTTP_200_OK

        if user:
            # Return success message
            token, created = Token.objects.get_or_create(user=user)
            response["data"] = {
                "token": token.key,
                "profile": HoustonUserSerializer(user).data,
                "message": "Login successful",
            }
        else:
            # Return error message
            response["error"] = ["Invalid username or password"]
            res_status = status.HTTP_400_BAD_REQUEST
    except Exception as e:
        response["error"] = [str(e)]
        res_status = status.HTTP_500_INTERNAL_SERVER_ERROR

    return JsonResponse(response, status=res_status)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout(request):
    response = {
        "status": status.HTTP_200_OK,
        "data": {},
        "error": [],
    }

    try:
        # Remove or invalidate the user's token
        request.user.auth_token.delete()
        response["data"] = {"message": "Logout successful"}
    except Exception as e:
        response["status"] = status.HTTP_500_INTERNAL_SERVER_ERROR
        response["error"] = [str(e)]

    return JsonResponse(response, status=response["status"])
