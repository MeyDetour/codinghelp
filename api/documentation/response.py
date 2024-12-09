

def get_response_routes():
    return   [
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
        }
        ,{
    "title": "Delete response",
    "method": "DELETE",
    "url": "api/response/{id}",
    "description": "Deletes a response and all associated votes.",
    "needToken": True,
    "bodyJson": {},
    "responseJson": {}
}

]

