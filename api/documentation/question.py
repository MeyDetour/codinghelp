def get_question_routes():
    return [
        {
            "title": "Create question",
            "method": "POST",
            "url": "api/question/new",
            "description": "Create a new question with the provided question content and directly associate it with at least one theme.",
            "needToken": True,
            "bodyJson": {"title": "string (NOT NULL)",
                "content": "string (NOT NULL)",
                "themes": ["int (NOT NULL)"]
            },
            "responseJson": {
                "id": "int (AI) (NOT NULL)",
                "created_at": "d.m.Y",
                "title": "string (NOT NULL)",
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
            "responseJson": {
                "title": "string (NOT NULL)",
                "id": "int (AI) (NOT NULL)",
                "created_at": "d.m.Y",
                "content": "string (NOT NULL)",
                "author": "int (NOT NULL)",
                "themes": [
                    "int (NOT NULL)"
                ],
                "isValidate": "boolean (NOT NULL)",
                "responses": [
                    {
                        "id": "int (AI) (NOT NULL)",
                        "created_at": "d.m.Y",
                        "content": "string (NOT NULL)",
                        "author": {

                            "image": "string (NULL)",
                            "username": "string (NOT NULL)",
                            "id": "int (AI) (NOT NULL)",
                        },
                        "upvote_count": "int (NOT NULL)",
                        "downvote_count": "int (NOT NULL)",
                        "question": "int (NOT NULL)"
                    }
                ]
            }
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
                "created_at": "d.m.Y",
                "title": "string (NOT NULL)",
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
            "title": "Edit question",
            "method": "PUT",
            "url": "api/question/{id}",
            "description": "Modify a question. The author and the validation status ('isValidate') cannot be updated through this endpoint. Validation occurs automatically if the question has fewer than 3 responses and at least one response has over 500 upvotes.",
            "needToken": True,
            "bodyJson": {
                "content": "string (NOT NULL)",
                "themes": ["int (NOT NULL)"],
                "title": "string (NOT NULL)",
            },
            "responseJson": {
                "id": "int (NOT NULL)",
                "created_at": "d.m.Y",
                "title": "string (NOT NULL)",
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
            "title": "Delete question",
            "method": "DELETE",
            "url": "api/question/{id}",
            "description": "Deletes a question along with all associated responses and the votes linked to those responses.",
            "needToken": True,
            "bodyJson": {},
            "responseJson": {
                "message": "string (NOT NULL)"
            }
        },
        {
            "title": "Add question to theme",
            "method": "PATCH",
            "url": "add/question/{questionId}/to/theme/{themeId}",
            "description": "Adds a question to a specific theme. Alternatively, you can use 'Edit question' to modify the list of themes directly.",
            "needToken": True,
            "bodyJson": {},
            "responseJson": {
                "message": "string (NOT NULL)"
            }
        }

    ]
