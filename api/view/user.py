from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializer import UserSerializer


# Create your views here.


@api_view(['GET','POST','PUT','DELETE'])
def get_user(request):
    return Response(UserSerializer({'name':"pascal","password":"aab"}).data)