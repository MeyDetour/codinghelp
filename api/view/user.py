from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from pycparser.ply.yacc import token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
import jwt, datetime
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from api.models import User
from api.serializer import UserSerializer


# Create your views here.

@api_view(['GET'])
def get_all_users(request):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET', 'PUT', 'DELETE'])
def get_user(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == 'GET':
        return Response(UserSerializer(user).data)

    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        pass


@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user =serializer.save()
    refresh = RefreshToken.for_user(user)
    return Response({
        'user': UserSerializer(user).data,
        'access_token': str(refresh.access_token),
        'refresh_token': str(refresh),
    }, status= 201)



@api_view(['GET'])
def get_profile(request):

    user = request.user
    return Response(UserSerializer(user).data)
