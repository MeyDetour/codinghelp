from datetime import datetime

from django.core.serializers import serialize
from django.template.context_processors import request
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import Question
from api.serializer import QuestionSerializer, UserSerializer
from api.view import is_authenticate


@api_view(['POST'])
def create_question(request):
    user = is_authenticate(request)
    if not user:
        return Response({"message": "Erreur lors de l'authentification"})


    if not request.data.get('content'):
        return Response({'message':"No content send"})

    data = request.data.copy()
    data['author']=user.id

    print(data)
    serializer = QuestionSerializer(data=data,partial=True)
    serializer.is_valid(raise_exception=True)
    question = serializer.save()
    print(question)
    return Response(QuestionSerializer(question).data)


@api_view(['GET','PUT','DELETE'])
def get_question(request,id):
    user = is_authenticate(request)
    if not user:
        return Response({"message": "Erreur lors de l'authentification"})

    question =  get_object_or_404(Question,pk=id)
    if request.method=='GET':
        return Response(QuestionSerializer(question).data)

    if request.method == "PUT":
        serializer = QuestionSerializer(instance=question,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    if request.method == 'DELETE':
        question.delete()
        return Response({'message':"ok"})
