from django.urls import path

from api.view import get_user, get_all_users, get_profile
from api.view.question import create_question, get_question
from api.view.theme import create_theme, get_themes, get_theme, add_question_to_theme

urlpatterns = [

    path('users/', get_all_users, name='get_users'),
    path('user/<int:id>', get_user, name='get_user'),

    path('profile', get_profile, name="profile"),


    path('question/new', create_question, name='create_question'),
    path('question/<int:id>', get_question, name='get_question'),
    path('add/question/<int:qutestionId>/to/theme/<int:themeId>', add_question_to_theme, name='add_question_to_theme'),
    path('themes', get_themes, name='get_themes'),
    path('theme/<int:id>', get_theme, name='get_theme'),
    path('theme/new', create_theme, name='create_theme'),

]