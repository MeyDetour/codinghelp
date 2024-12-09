from django.shortcuts import render
from django.template.context_processors import request


from api.documentation import get_user_routes, get_theme_routes, get_question_routes, get_response_routes, \
    get_vote_routes


def render_doc(request):
    # juste render doc like name indicate
    data = {
        "User":get_user_routes() ,
        "Theme" : get_theme_routes() ,
        "Question":get_question_routes(),
        "Response":  get_response_routes() ,
        "Vote":get_vote_routes()}
    print(data)

    return render(request, 'api/base.html', {"themes":data})
