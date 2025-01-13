from datetime import datetime

from django.core.serializers import serialize
from django.template.context_processors import request
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import Question, Theme
from api.serializer import QuestionSerializer, UserSerializer, QuestionDetailsSerializer
from api.view import is_authenticate


@api_view(['POST'])
def create_question(request):
    # create question with question content and associate directly minimum  one theme
    user = is_authenticate(request)
    if not user:
        return Response({"message": "error during authentication"},401)

    if not request.data.get('title'):
        return Response({'message': "No title send"},406)

    if not request.data.get('content'):
            return Response({'message': "No content send"},406)
    if not request.data.get('contentHTML'):
            return Response({'message': "No contentHTML send"},406)

    if Question.objects.filter(title__iexact=request.data.get('title')).exists():
        return Response({"message": "Question with this title already exists"}, status=409)

    theme_ids = request.data.get('themes', [])
    if not isinstance(theme_ids, list) or not theme_ids:
        return Response({'message': "please send a list of themes id"}, status=400)

    themes = Theme.objects.filter(id__in=theme_ids)
    if themes.count() != len(theme_ids):
        return Response({'message': "this theme doesnt exist"}, status=404)


    data = request.data.copy()
    #auto add author

    serializer = QuestionDetailsSerializer(data=data, partial=True)
    serializer.is_valid(raise_exception=True)
    question = serializer.save()
    question.author=user.id
    question.save()
    return Response(QuestionDetailsSerializer(question).data)


@api_view(['GET'])
def get_questions(request):
    # get all questions ( function principaly used on debug )
    # not use in front end because all questions are associated
    # with one theme, we get all questions of one theme not only all questions
    user = is_authenticate(request)
    if not user:
        return Response({"message": "error during authentication"},401)

    themes = Question.objects.all()
    serializer = QuestionSerializer(themes, many=True)
    return (Response(serializer.data))


@api_view(['GET', 'PUT', 'DELETE'])
def get_question(request, id):
    # get one question and all response associated with
    # edit one question
    # delete question and all response associated and all vote associated
    user = is_authenticate(request)
    if not user:
        return Response({"message": "error during authentication"},401)

    question = get_object_or_404(Question, pk=id)
    if question.author == None:
        question.delete()

        return Response({"message": "No author of question"},400)

    if request.method == 'GET':
        return Response(QuestionDetailsSerializer(question).data)

    if request.method == "PUT":
        if question.author.id != user.id:
            return Response({"message": "You can't edit this"}, status=403)
        if request.data.get('isValidate'):
            return Response({"message": "Cannot validate question"}, status=403)

        serializer = QuestionSerializer(instance=question, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    if request.method == 'DELETE':
        if question.author.id != user.id and not user.is_superuser:
            return Response({"message": "You can't delete this"}, status=403)

        if question.responses.exists():
            return Response({"message": "You can't delete this there are many responses"}, status=403)

        question.delete()
        return Response({'message': "ok"})
