from datetime import datetime

from django.core.serializers import serialize
from django.template.context_processors import request
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import Question, Theme
from api.serializer import QuestionSerializer,  ResponseSerializer
from api.view import is_authenticate


@api_view(['POST'])
def create_response(request):
    # create response with response content and associate directly minimum  one theme
    user = is_authenticate(request)
    if not user:
        return Response({"message": "Erreur lors de l'authentification"})

    if not request.data.get('content'):
        return Response({'message': "No content send"})


    question_id = request.data.get('question')

    if not request.data.get('question'):
        return Response({'message': "No question attached"})

    try :
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        return Response({'message': "Question wanted doesnt exist"}, status=404)


    data = request.data.copy()
    data['author'] = user.id
    data['question'] = question.id

    serializer = ResponseSerializer(data=data, partial=True)
    serializer.is_valid(raise_exception=True)
    response =   serializer.save()
    return Response(ResponseSerializer(response).data,status=201)


@api_view(['GET'])
def get_responses(request):
    # get all responses ( function principaly used on debug )
    user = is_authenticate(request)
    if not user:
        return Response({"message": "Erreur lors de l'authentification"})

    themes = Question.objects.all()
    serializer = QuestionSerializer(themes, many=True)
    return (Response(serializer.data))


@api_view(['GET', 'PUT', 'DELETE'])
def get_response(request, id):
    # get one response and all response associated with
    user = is_authenticate(request)
    if not user:
        return Response({"message": "Erreur lors de l'authentification"}, status=400)

    response = get_object_or_404(Question, pk=id)
    if response.author == None:
        response.delete()

        return Response({"message": "Question deleted"})

    if request.method == 'GET':
        return Response(QuestionSerializer(response).data)

    if request.method == "PUT":
        if response.author.id != user.id:
            return Response({"message": "You can't delete this"}, status=403)

        serializer = QuestionSerializer(instance=response, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    if request.method == 'DELETE':
        if response.author.id != user.id:
            return Response({"message": "You can't delete this"}, status=403)

        response.delete()
        return Response({'message': "ok"})
