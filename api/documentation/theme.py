

def get_theme_routes():
    return   [
        {
            'title': 'Get themes',
            'method': 'GET',
            'url': '/api/themes',
            'description': ' ',
            'needToken': True,
            'bodyJson': {}
            ,
            "responseJson": [{}]
        },       {
            'title': 'Get theme',
            'method': 'GET',
            'url': '/api/theme/{id}',
            'description': ' ',
            'needToken': True,
            'bodyJson': {}
            ,
            "responseJson": [{}]
        },      {
            'title': 'Edit theme',
            'method': 'PUT',
            'url': '/api/theme/{id}',
            'description': ' ',
            'needToken': True,
            'bodyJson': {}
            ,
            "responseJson": [{}]
        },    {
            'title': 'Delete theme',
            'method': 'DELETE',
            'url': '/api/theme/{id}',
            'description': ' ',
            'needToken': True,
            'bodyJson': {}
            ,
            "responseJson": [{}]
        },    {
            'title': 'Create theme',
            'method': 'POST',
            'url': '/api/theme/new',
            'description': ' ',
            'needToken': True,
            'bodyJson': {}
            ,
            "responseJson": [{}]
        },
]