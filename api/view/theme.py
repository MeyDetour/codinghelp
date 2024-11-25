from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.models import Theme, Question
from api.serializer import QuestionSerializer, ThemeSerializer
from api.view import is_authenticate


@api_view(['GET'])
def get_themes(request):
    user = is_authenticate(request)
    if not user:
        return Response({"message": "Erreur lors de l'authentification"})

    themes = Theme.objects.all()
    serializer = ThemeSerializer(themes,many=True)
    return (Response(serializer.data))

@api_view(['GET',"PUT","DELETE"])
def get_theme(request,id):
    user = is_authenticate(request)
    if not user:
        return Response({"message": "Erreur lors de l'authentification"})

    theme = get_object_or_404(Theme,id=id)
    if theme.author == None:
        theme.delete()
    if request.method == 'GET':
         return Response(ThemeSerializer(theme).data)
    if request.method == "PUT":

        if theme.author.id != user.id:
            return Response({"message": "You can't delete this"}, status=403)

        serializer = ThemeSerializer(instance=theme,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return  Response(serializer.data)

    if request.method == "DELETE":
        if theme.author.id != user.id:
            return Response({"message": "You can't delete this"}, status=403)

        theme.delete()
        return  Response({'message':"ok"})


@api_view(['POST'])
def create_theme(request):
    user = is_authenticate(request)
    if not user:
        return Response({"message": "Erreur lors de l'authentification"})

    if not request.data.get('name'):
        return Response({"message":"Please enter name"})

    data = request.data.copy()
    data['author'] = user.id
    print(data)
    serializer = ThemeSerializer(data=data, partial=True)
    serializer.is_valid(raise_exception=True)
    question = serializer.save()
    print(question)
    return Response({'message': 'ok'})

@api_view(['PATCH'])
def add_question_to_theme(request,qutestionId,themeId):
    user = is_authenticate(request)
    if not user:
        return Response({"message": "Erreur lors de l'authentification"})

    theme = get_object_or_404(Theme, id=themeId)
    question = get_object_or_404(Question, id=qutestionId)

    question.theme = theme
    question.save()

    return Response({'message': 'ok'})


