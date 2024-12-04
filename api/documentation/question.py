

def get_user_routes():
    return   [
     {
            'title': 'Create question',
            'method': 'POST',
            'url': 'api/question/new',
            'description': '',
            'needToken': True,
            'bodyJson': {}
            ,
            "responseJson": [{}]
        },{
            'title': 'Get question',
            'method': 'GET',
            'url': 'api/question/{id}',
            'description': '',
            'needToken': True,
            'bodyJson': {}
            ,
            "responseJson": [{}]
        },{
            'title': 'Get questions',
            'method': 'GET',
            'url': 'api/questions',
            'description': '',
            'needToken': True,
            'bodyJson': {}
            ,
            "responseJson": [{}]
        },{
            'title': 'Edit question',
            'method': 'PUT',
            'url': 'api/question/{id}',
            'description': '',
            'needToken': True,
            'bodyJson': {}
            ,
            "responseJson": [{}]
        },{
            'title': 'Delete question',
            'method': 'DELETE',
            'url': 'api/question/{id}',
            'description': '',
            'needToken': True,
            'bodyJson': {}
            ,
            "responseJson": [{}]
        },{
            'title': 'Add question to theme',
            'method': 'PATCH',
            'url': 'add/question/{qutestionId}/to/theme/{themeId}',
            'description': '',
            'needToken': True,
            'bodyJson': {}
            ,
            "responseJson": [{}]
        }
]