from django.urls import path

from api.view import get_user

urlpatterns = [
    path('user/', get_user, name='get_user'),
]