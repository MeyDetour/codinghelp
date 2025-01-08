from django.conf.urls.static import static
from django.urls import path

from api.view import get_user, get_all_users, get_profile, create_response, delete_response, \
    to_downvote_response, to_upvote_response, follow_user, get_field_of_user, get_field_of_current_user , upload_image,unfollow_user
from api.view.question import create_question, get_question, get_questions
from api.view.theme import create_theme, get_themes, get_theme, add_question_to_theme
from coding import settings

urlpatterns = [
    # ======================= USER

    path('users/', get_all_users, name='get_users'),
    path('user/<int:id>', get_user, name='get_user'),

    path('user/<int:id>/<str:field>', get_field_of_user, name='get_field_of_user'),
    path('profile/<str:field>', get_field_of_current_user, name='get_field_of_current_user'),
    path('profile', get_profile, name="profile"),
    path('follow/user/<int:id>', follow_user, name="follow_user"),
    path('unfollow/user/<int:id>', unfollow_user, name="unfollow_user"),
    path('upload/image/to/profile', upload_image, name="image_upload"),

    # ======================= THEMES
    path('themes', get_themes, name='get_themes'),
    path('theme/<int:id>', get_theme, name='get_theme'),
    path('theme/new', create_theme, name='create_theme'),

    # ======================= QUESTION
    path('question/new', create_question, name='create_question'),
    path('question/<int:id>', get_question, name='get_question'),
    path('questions', get_questions, name='get_questions'),
    path('add/question/<int:qutestionId>/to/theme/<int:themeId>', add_question_to_theme, name='add_question_to_theme'),

    # ======================= RESPONSE
    path('response/new', create_response, name='create_reponse'),
    path('response/<int:id>', delete_response, name='delete_response'),

    # ======================= UPVOTE
    path('upvote/<int:response_id>', to_upvote_response, name='to_upvote_response'),
    path('downvote/<int:response_id>', to_downvote_response, name='to_downvote_response'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

