from django.contrib.auth import authenticate
from django.db.models import Count
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
from api.serializer import UserSerializer, QuestionSerializer, ResponseSerializer


def is_authenticate(request):
    # function used in all function to verify if
    # there is one user connected, it return user or none
    jwt_authenticator = JWTAuthentication()

    print("En-têtes reçus :", request.headers)
    try:
        user, token = jwt_authenticator.authenticate(request)

    except Exception as e:
        print("error during authentication :", e)
        return None
    # Vérifiez si l'utilisateur est bien authentifié
    if not user:
        return None
    return user


# Create your views here.

@api_view(['GET'])
def get_all_users(request):
    # get all user may not be used in front end
    # this request return juste simple informations of user
    user = is_authenticate(request)
    if not user:
        return Response({"message": "error during authentication"},401)

    users = User.objects.all()
    users = users.annotate(
        questions_count=Count('questions'),
        responses_count=Count('responses'),
        followers_count=Count('followers'),
        following_count=Count('followings')
    )
    users = users.order_by('-questions_count', '-responses_count', '-followers_count', '-following_count')

    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET' ])
def get_user(request, id):
    # this request return all informations about
    # user and its activity
    user = is_authenticate(request)
    if not user:
        return Response({"message": "error during authentication"},401)

    user_to_get = get_object_or_404(User, id=id)

    return Response(UserSerializer(user_to_get).data)



@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):

    #create account with email username and password
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response({"message":"ok"
    }, status=201)


@api_view(['GET','PUT','DELETE'])
def get_profile(request):

    # get profilte
    # edit profile : we cant change password here
    # delete profile ( in progress )
    # we dont want to delete all question created by use
    # we want to create an "deleted user" and associate question to him
    user = is_authenticate(request)

    if not user:
        return Response({"message": "error during authentication"},401)


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

@api_view(['GET'])
def get_field_of_user(request,id,field):
    user = is_authenticate(request)

    if not user:
        return Response({"message": "error during authentication"},401)

    if field not in ['questions',"followers","followings","responses"]:
        return Response({"message": "search field must be in questions or followers or followings or responses"})
    user_to_get = get_object_or_404(User, id=id)

    if field == 'questions':
        serializer =  QuestionSerializer(user_to_get.questions.all(), many=True)
    elif field == 'followers':
        users = user_to_get.followings.annotate(
            questions_count=Count('questions'),
            responses_count=Count('responses'),
            followers_count=Count('followers'),
            following_count=Count('followings')
        )
        users = users.order_by('-questions_count', '-responses_count', '-followers_count', '-following_count')

        serializer = UserSerializer(users, many=True)


    elif field == 'followings':
        users = user_to_get.followers.annotate(
            questions_count=Count('questions'),
            responses_count=Count('responses'),
            followers_count=Count('followers'),
            following_count=Count('followings')
        )
        users = users.order_by('-questions_count', '-responses_count', '-followers_count', '-following_count')

        serializer = UserSerializer(users, many=True)


    elif field == 'responses':
        serializer = ResponseSerializer(user_to_get.responses.all(), many=True)

    return Response(serializer.data)
@api_view(['GET'])
def get_field_of_current_user(request,field):
    user = is_authenticate(request)

    if not user:
        return Response({"message": "error during authentication"},401)

    if field not in ['questions',"followers","followings","responses"]:
        return Response({"message": "search field must be in questions or followers or followings or responses"})

    if field == 'questions':
        serializer =  QuestionSerializer(user.questions.all(), many=True)
    elif field == 'followers':
        users = user.followings.annotate(
            questions_count=Count('questions'),
            responses_count=Count('responses'),
            followers_count=Count('followers'),
            following_count=Count('followings')
        )
        users = users.order_by('-questions_count', '-responses_count', '-followers_count', '-following_count')

        serializer = UserSerializer(users, many=True)


    elif field == 'followings':
        users = user.followers.annotate(
            questions_count=Count('questions'),
            responses_count=Count('responses'),
            followers_count=Count('followers'),
            following_count=Count('followings')
        )
        users = users.order_by('-questions_count', '-responses_count', '-followers_count', '-following_count')

        serializer = UserSerializer(users, many=True)


    elif field == 'responses':
        serializer = ResponseSerializer(user.responses.all(), many=True)

    return Response(serializer.data)


@api_view(['PATCH'])
def follow_user(request,id):

    #follow user with id, we appear in followers and he appear in following
    # we cant follow itself
    user = is_authenticate(request)
    if not user:
        return Response({"message": "error during authentication"},401)
    if user.id == id:
        return Response({"message": "Unauthorized"}, status=403)

    user2 = get_object_or_404(User,pk=id)
    user.following.add(user2)
    user.save()
    return Response({"message": "ok"}, status=200)


@api_view(['PATCH'])
def upload_image(request):
    user = is_authenticate(request)
    if not user:
        return Response({"message": "error during authentication"},401)

    image =request.FILES.get('image')
    if not image :
        return Response({"message": "Please provide an image"})

    user.image = image
    user.save()

    return Response({"message": "ok"})