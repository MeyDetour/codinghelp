from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    print("the exception :",response)
    if isinstance(exc, NotFound):
        return Response(
            {"error": "Resource not found"},
            status=404
        )
    return response
