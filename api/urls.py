from django.urls import path

from api.view import get_user, create_user, get_all_users

urlpatterns = [
    path('users/', get_all_users, name='get_users'),
    path('user/<int:id>', get_user, name='get_user'),
    path('create/user/', create_user, name='createuser'),
]