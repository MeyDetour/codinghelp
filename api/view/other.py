from django.shortcuts import render
from django.template.context_processors import request


from api.documentation import get_user_routes, get_theme_routes


def render_doc(request):

    data = get_user_routes()  + get_theme_routes()
    print(data)

    return render(request, 'api/base.html', {"routes":data})
