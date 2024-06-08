from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.models import GithubCred
from api.serializers import GithubCredSerializer
from django.http import JsonResponse

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def fetch(request):
    response = {
        "status": status.HTTP_200_OK,
        "data": {},
        "error": [],
    }

    try:
        user = request.user
        creds = GithubCred.objects.filter(user=user)
        serializer = GithubCredSerializer(creds, many=True)
        response["data"] = serializer.data
    except Exception as e:
        response["status"] = status.HTTP_500_INTERNAL_SERVER_ERROR
        response["error"] = [str(e)]

    return JsonResponse(response, status=response["status"])

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create(request):
    response = {
        "status": status.HTTP_200_OK,
        "data": {},
        "messager": "",
        "error": [],
    }

    try:
        user = request.user
        data = request.data

        serializer = GithubCredSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=user)
            response["data"] = serializer.data
            response["message"] = "GitHub credential added successfully"
            response["status"] = status.HTTP_201_CREATED
        else:
            response["status"] = status.HTTP_400_BAD_REQUEST
            response["error"] = [value for key, value in serializer.errors.items()]
    except Exception as e:
        response["status"] = status.HTTP_500_INTERNAL_SERVER_ERROR
        response["error"] = [str(e)]
    
    return JsonResponse(response, status=response["status"])
