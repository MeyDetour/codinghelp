def get_user_routes():
    return [
        {
            "title": "Create question",
            "method": "POST",
            "url": "api/question/new",
            "description": "Create a new question with the provided question content and directly associate it with at least one theme.",
            "needToken": True,
            "bodyJson": {
                "content": "string (NOT NULL)",
                "themes": ["int (NOT NULL)"]
            },
            "responseJson": {
                "id": "int (AI) (NOT NULL)",
                "content": "string (NOT NULL)",
                "author": "int (NOT NULL)",
                "themes": [
                    "int (NOT NULL)"
                ],
                "isValidate": "boolean (NOT NULL)",
                "responses_count": "int (NOT NULL)"
            }
        }
        , {
            "title": "Get question",
            "method": "GET",
            "url": "api/question/{id}",
            "description": "Get one question and all responses associated with it.",
            "needToken": True,
            "bodyJson": {},
            "responseJson": [{
                "id": "int (AI) (NOT NULL)",
                "content": "string (NOT NULL)",
                "author": "int (NOT NULL)",
                "themes": [
                    "int (NOT NULL)"
                ],
                "isValidate": "boolean (NOT NULL)",
                "responses": [
                    {
                        "id": "int (AI) (NOT NULL)",
                        "content": "string (NOT NULL)",
                        "author": "int (NOT NULL)",
                        "upvote_count": "int (NOT NULL)",
                        "downvote_count": "int (NOT NULL)",
                        "question": "int (NOT NULL)"
                    }
                ]
            }]
        }

















        , {
            "title": "Get questions",
            "method": "GET",
            "url": "api/questions",
            "description": "Get all questions (function mainly used for debugging). Not used in frontend because all questions are associated with many themes. To get questions, one must query the theme and retrieve all associated questions.",
            "needToken": True,
            "bodyJson": {},
            "responseJson": [{
                "id": "int (NOT NULL)",
                "content": "string (NOT NULL)",
                "author": "int (NOT NULL)",
                "themes": [
                    "int (NOT NULL)"
                ],
                "isValidate": "boolean (NOT NULL)",
                "responses_count": "int (NOT NULL)"
            }]
        }
        , {
            'title': 'Edit question',
            'method': 'PUT',
            'url': 'api/question/{id}',
            'description': '',
            'needToken': True,
            'bodyJson': {}
            ,
            "responseJson": [{}]
        }, {
            'title': 'Delete question',
            'method': 'DELETE',
            'url': 'api/question/{id}',
            'description': '',
            'needToken': True,
            'bodyJson': {}
            ,
            "responseJson": [{}]
        }, {
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
