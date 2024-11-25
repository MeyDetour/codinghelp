

def get_user_routes():
    return   [
        {
            'title': 'Register',
            'method': 'POST',
            'url': '/register',
            'description': 'This request retrieves all books in the system. One book can be in multiple bookshelves, and each bookshelf can contain many books.',
            'needToken': False,
            'bodyJson': {
                "searchTerm": "string (NOT NULL)"
            }
            ,
            "responseJson": [{
                "bookshelves": [
                    {
                        "_id": "string (AI) (NOT NULL)",
                        "name": "string (NOT NULL)"
                    }
                ],
                "_id": "string (AI) (NOT NULL)",
                "author": "string (NULL)",
                "ine": "string (NULL)",
                "image": "url (NULL)",
                "description": "string (NULL)",
                "title": "string (NOT NULL)"
            }]
        },
        {
            'title': 'Login',
            'method': 'POST',
            'url': '/login',
            'description': ' ',
            'needToken': False,
            'bodyJson': {}
            ,
            "responseJson": [{}]
        } ,{
            'title': 'Refresh Token',
            'method': 'GET',
            'url': 'api/token/refresh/',
            'description': '',
            'needToken': False,
            'bodyJson': {}
            ,
            "responseJson": [{}]
        } ,{
            'title': 'Get all users',
            'method': 'GET',
            'url': 'api/users/',
            'description': '',
            'needToken': False,
            'bodyJson': {}
            ,
            "responseJson": [{}]
        },{
            'title': 'Get one user',
            'method': 'GET',
            'url': 'api/user/{id}',
            'description': '',
            'needToken': False,
            'bodyJson': {}
            ,
            "responseJson": [{}]
        },{
            'title': 'Get profile',
            'method': 'GET',
            'url': 'api/profile',
            'description': '',
            'needToken': True,
            'bodyJson': {}
            ,
            "responseJson": [{}]
        },{
            'title': 'Edit profile',
            'method': 'PUT',
            'url': 'api/profile',
            'description': '',
            'needToken': True,
            'bodyJson': {}
            ,
            "responseJson": [{}]
        },{
            'title': 'Delete profile',
            'method': 'DELETE',
            'url': 'api/profile',
            'description': '',
            'needToken': True,
            'bodyJson': {}
            ,
            "responseJson": [{}]
        }
]