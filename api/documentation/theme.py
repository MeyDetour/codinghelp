def get_theme_routes():
    return [
        {
            "title": "Get themes",
            "method": "GET",
            "url": "/api/themes",
            "description": "Retrieves all themes without detailed questions information, optimized for frontend usage to avoid transferring unnecessary data.",
            "needToken": True,
            "bodyJson": {},
            "responseJson": [
                {
                    "id": "int (AI) (NOT NULL)",
                    "name": "string (NOT NULL)",
                    "author": "int (NOT NULL)",
                    "questions_count": "int (NOT NULL)",
                    "contributor_count": "int (NOT NULL)"
                }
            ]
        }
        , {
            "title": "Get theme",
            "method": "GET",
            "url": "/api/theme/{id}",
            "description": "Retrieves theme information along with all its questions without detailed responses or votes.",
            "needToken": True,
            "bodyJson": {},
            "responseJson": [
                {
                    "id": "int (AI) (NOT NULL)",
                    "name": "string (NOT NULL)",
                    "author": "int (NOT NULL)",
                    "questions": [
                        {
                            "id": "int (AI) (NOT NULL)",
                            "created_at": "date (NOT NULL)",
                            "content": "string (NOT NULL)",
                            "author": "int (NOT NULL)",
                            "themes": ["int (NOT NULL)"],
                            "isValidate": "boolean (NOT NULL)",
                            "responses_count": "int (NOT NULL)"
                        }
                    ]
                }
            ]
        }
        , {
            "title": "Edit theme",
            "method": "PUT",
            "url": "/api/theme/{id}",
            "description": "Modifies the name of the theme without changing any associations between questions and themes.",
            "needToken": True,
            "bodyJson": {
                "name": "string (NOT NULL)"
            },
            "responseJson":  {
                "message": "ok"
            }
        }
        , {
            "title": "Delete theme",
            "method": "DELETE",
            "url": "/api/theme/{id}",
            "description": "Deletes the theme if no questions are associated with it. If there are questions linked to the theme, deletion will be prevented.",
            "needToken": True,
            "bodyJson": {},
            "responseJson": {
                "message": "ok"
            }
        }
        , {
            "title": "Create theme",
            "method": "POST",
            "url": "/api/theme/new",
            "description": "Creates a new theme with a specified name. The theme is associated with the authenticated user as the author.",
            "needToken": True,
            "bodyJson": {
                "name": "string (NOT NULL)"
            },
            "responseJson": {
                "message": "ok"
            }
        }

    ]
