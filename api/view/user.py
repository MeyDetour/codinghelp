from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from pycparser.ply.yacc import token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
import jwt, datetime
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from api.models import User
from api.serializer import UserSerializer, UserDetailsSerializer


def is_authenticate(request):

    jwt_authenticator = JWTAuthentication()

    try:
        user, token = jwt_authenticator.authenticate(request)

    except Exception as e:
        print("Erreur lors de l'authentification :", e)
        return None
    # Vérifiez si l'utilisateur est bien authentifié
    if not user:
        return None
    return user


# Create your views here.

@api_view(['GET'])
def get_all_users(request):
    user = is_authenticate(request)
    if not user:
        return Response({"message": "Erreur lors de l'authentification"})

    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET' ])
def get_user(request, id):
    user = is_authenticate(request)
    if not user:
        return Response({"message": "Erreur lors de l'authentification"})

    user_to_get = get_object_or_404(User, id=id)

    return Response(UserDetailsSerializer(user_to_get).data)



@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):

    serializer = UserSerializer(data=request.data)
    print(request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    refresh = RefreshToken.for_user(user)
    return Response({"message":"ok"
    }, status=201)


@api_view(['GET','PUT','DELETE'])
def get_profile(request):
    user = is_authenticate(request)

    if not user:
        return Response({"message": "Erreur lors de l'authentification"})


    if request.method == 'GET':

        return Response(UserSerializer(user).data)

    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        user.delete()

        return Response({"message":"ok"}, status=200)



@api_view(['PATCH'])
def follow_user(request,id):

    user = is_authenticate(request)
    if not user:
        return Response({"message": "Erreur lors de l'authentification"})
    if user.id != id:
        return Response({"message": "Vous n'êtes pas autorisé à voir cet utilisateur"}, status=403)

    user2 = get_object_or_404(User,pk=id)
    user.following.add(user2)
    user.save()
    return Response({"message": "ok"}, status=200)

