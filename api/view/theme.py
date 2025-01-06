from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.models import Theme, Question
from api.serializer import  ThemeDetailSerializer, ThemeListSerializer
from api.view import is_authenticate


@api_view(['GET'])
def get_themes(request):
    #get all theme without details

    user = is_authenticate(request)
    if not user:
        return Response({"message": "error during authentication"})

    themes = Theme.objects.all()
    serializer = ThemeListSerializer(themes,many=True)

    return (Response(serializer.data))

@api_view(['GET',"PUT","DELETE"])
def get_theme(request,id):
    #get one theme and list of question
    # edit theme name
    # delete the theme if the are no questions associated
    user = is_authenticate(request)
    if not user:
        return Response({"message": "error during authentication"})

    theme = get_object_or_404(Theme,id=id)
    if theme.author == None:
        theme.delete()
    if request.method == 'GET':
         return Response(ThemeDetailSerializer(theme).data)
    if request.method == "PUT":

        if theme.author.id != user.id:
            return Response({"message": "You can't delete this"}, status=403)

        serializer = ThemeDetailSerializer(instance=theme,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "ok"})

    if request.method == "DELETE":
        if theme.author.id != user.id:
            return Response({"message": "You can't delete this"}, status=403)
        if not theme.questions.exists():
             theme.delete()
             return  Response({'message':"ok"})
        return Response({"message": "Cannot delete a theme with associated questions"}, status=400)

@api_view(['POST'])
def create_theme(request):
    #create theme with juste a name
    user = is_authenticate(request)
    if not user:
        return Response({"message": "error during authentication"})

    if not request.data.get('name'):
        return Response({"message":"Please enter name"},406)

    existingTheme = Theme.objects.filter(name=request.data.get('name'))
    if existingTheme.exists() :
        return Response({"message": "Theme with this name already exist"}, 409)

    data = request.data.copy()
    data['author'] = user.id
    serializer = ThemeDetailSerializer(data=data, partial=True)
    serializer.is_valid(raise_exception=True)
    theme = serializer.save()
    return Response(ThemeListSerializer(theme).data)

@api_view(['PATCH'])
def add_question_to_theme(request,qutestionId,themeId):
    # after creating theme and question we can associate many question to many theme
    # here is the function to add one question to one theme
    user = is_authenticate(request)
    if not user:
        return Response({"message": "error during authentication"})

    theme = get_object_or_404(Theme, id=themeId)
    question = get_object_or_404(Question, id=qutestionId)

    question.theme = theme
    question.save()

    return Response({'message': 'ok'})


