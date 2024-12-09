from datetime import datetime

from django.core.serializers import serialize
from django.template.context_processors import request
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from api.models import Question, Theme,ResponseText
from api.serializer import QuestionSerializer, ResponseSerializer
from api.view import is_authenticate


@api_view(['POST'])
def create_response(request):
    # create response with  content and associate it to question
    # we get all responses directly in question
    user = is_authenticate(request)
    if not user:
        return Response({"message": "Erreur lors de l'authentification"})

    if not request.data.get('content'):
        return Response({'message': "No content send"})

    question_id = request.data.get('question')

    if not request.data.get('question'):
        return Response({'message': "No question attached"})

    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        return Response({'message': "Question does not exist"}, status=404)

    data = request.data.copy()
    # auto add author
    data['author'] = user.id
    data['question'] = question.id
    print(data)

    serializer = ResponseSerializer(data=data, partial=True)
    serializer.is_valid(raise_exception=True)
    response = serializer.save()
    return Response(ResponseSerializer(response).data, status=201)


@api_view([ 'DELETE'])
def delete_response(request, id):

    # we dont want user to edit response after send it
    # user can only delete
    # delete response delete also all votes associated
    user = is_authenticate(request)
    if not user:
        return Response({"message": "Erreur lors de l'authentification"}, status=400)

    response = get_object_or_404(ResponseText, pk=id)
    if response.author == None:
        response.delete()
        return Response({"message": "Response deleted"})

    # if request.method == "PUT":
    #     if response.author.id != user.id:
    #         return Response({"message": "You can't delete this"}, status=403)
    #
    #     serializer = QuestionSerializer(instance=response, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)

    if request.method == 'DELETE':
        if response.author.id != user.id and not user.is_superuser:
            return Response({"message": "You can't delete this"}, status=403)

        response.delete()
        return Response({'message': "ok"})
