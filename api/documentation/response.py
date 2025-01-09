def get_response_routes():
    return [
         {
            "title": "Get response ",
            "method": "GET",
            "url": "api/question/{id}",
            "description": "You can get one response and get all responses of one question in the same request of 'get question'.",
            "needToken": True,
            "bodyJson": {},
            "responseJson": {}
        },
        {
            "title": "Create response",
            "method": "POST",
            "url": "api/response/new",
            "description": "Creates a response with its content. The author is automatically assigned.",
            "needToken": True,
            "bodyJson": {
                "content": "string (NOT NULL)",
                "question": "int (NOT NULL)"
            },
            "responseJson": {
                "id": "int (AI) (NOT NULL)",
                "created_at": "d.m.Y",
                "content": "string (NOT NULL)",
                "author": "int (NOT NULL)",
                "upvote_count": "int",
                "downvote_count": "int",
                "question": "int (NOT NULL)"
            }
        }, {
            "title": "Edit response",
            "method": "NONE",
            "url": "no path",
            "description": "You can't edit response. It's my choice",
            "needToken": True,
            "bodyJson": {   },
            "responseJson": {   }
        }
        , {
            "title": "Delete response",
            "method": "DELETE",
            "url": "api/response/{id}",
            "description": "Deletes a response and all associated votes.",
            "needToken": True,
            "bodyJson": {},
            "responseJson": {}
        }

    ]
