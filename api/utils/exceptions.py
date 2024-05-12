from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotAuthenticated, PermissionDenied

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if isinstance(exc, NotAuthenticated):
            response.data = {
                "status": status.HTTP_401_UNAUTHORIZED,
                "data": {},
                "error": ["User is not authenticated"]
            }
            response.status_code = status.HTTP_401_UNAUTHORIZED
        elif isinstance(exc, PermissionDenied):
            response.data = {
                "status": status.HTTP_403_FORBIDDEN,
                "data": {},
                "error": ["Permission denied"]
            }
            response.status_code = status.HTTP_403_FORBIDDEN

    return response
