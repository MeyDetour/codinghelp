def get_user_routes():
    return [
        {
            "title": "Register",
            "method": "POST",
            "url": "/register",
            "description": "Create a new account by providing an email, username, and password. This will register the user in the system.",
            "needToken": False,
            "bodyJson": {
                "email": "string (NOT NULL)",
                "username": "string (NOT NULL)",
                "password": "string (NOT NULL)"
            },
            "responseJson": {
                "message": "ok"
            }
        }
        ,
        {
            "title": "Login",
            "method": "POST",
            "url": "/login",
            "description": "Allows the user to log in using their email and password, and obtain authentication tokens for further requests.",
            "needToken": False,
            "bodyJson": {
                "email": "string (NOT NULL)",
                "password": "string (NOT NULL)"
            },
            "responseJson": {
                "refresh": "string (NOT NULL)",
                "access": "string (NOT NULL)"
            }
        }
        , {
            "title": "Refresh Token",
            "method": "POST",
            "url": "api/token/refresh/",
            "description": "Regenerates a new access token using a valid refresh token.",
            "needToken": False,
            "bodyJson": {
                "refresh": "string (NOT NULL)"
            },
            "responseJson": {
                "access": "string (NOT NULL)"
            }
        }
        , {
            "title": "Get all users",
            "method": "GET",
            "url": "api/users/",
            "description": "Fetches all users, sorted by activity such as the number of responses and questions asked, including the number of followers and following.",
            "needToken": True,
            "bodyJson": {},
            "responseJson": [
                {
                    "image":"string (NULL)",
                    "first_name": "string (NULL)",
                    "last_name": "string (NULL)",
                    "id": "int (NOT NULL)",
                    "last_login": "datetime (NULL)",
                    "is_superuser": "boolean (NOT NULL)",
                    "email": "string (NOT NULL)",
                    "is_staff": "boolean (NOT NULL)",
                    "username": "string (NOT NULL)",
                    "questions_count": "int (NOT NULL)",
                    "themes_count": "int (NOT NULL)",
                    "votes_count": "int (NOT NULL)",
                    "responses_count": "int (NOT NULL)",
                    "followers_count": "int (NOT NULL)",
                    "followings_count": "int (NOT NULL)",

                }
            ]
        }
        , {
            "title": "Get one user",
            "method": "GET",
            "url": "api/user/{id}",
            "description": "Fetches the basic details of a specific user without statistics (responses, questions, followers, etc.). Additional requests are needed to retrieve these details.",
            "needToken": True,
            "bodyJson": {},
            "responseJson": {
                    "image":"string (NULL)",
                "first_name": "string (NULL)",
                "last_name": "string (NULL)",
                "id": "int (NOT NULL)",
                "last_login": "datetime (NULL)",
                "is_superuser": "boolean (NOT NULL)",
                "email": "string (NOT NULL)",
                "is_staff": "boolean (NOT NULL)",
                "username": "string (NOT NULL)",
                "questions_count": "int (NOT NULL)",
                "themes_count": "int (NOT NULL)",
                "votes_count": "int (NOT NULL)",
                "responses_count": "int (NOT NULL)",
                "followers_count": "int (NOT NULL)",
                "followings_count": "int (NOT NULL)",

            }
        }
        ,
        {
            "title": "Get questions of one user",
            "method": "GET",
            "url": "api/user/{id}/questions",
            "description": "Fetches all questions of a specific user. You can also get the user's responses, followers, and followings by replacing 'questions' with 'responses', 'followers', or 'followings' in the URL.",
            "needToken": True,
            "bodyJson": {},
            "responseJson": [
                {
                    "id": "int (NOT NULL)",
                    "created_at": "string (NOT NULL)",
                    "content": "string (NOT NULL)",
                    "author": "int (NOT NULL)",
                    "themes": [
                        "int (NOT NULL)"
                    ],
                    "isValidate": "boolean (NOT NULL)",
                    "responses_count": "int (NOT NULL)"
                }
            ]
        }, {
            "title": "Get responses of one user",
            "method": "GET",
            "url": "api/user/{id}/responses",
            "description": "Fetches all responses of a specific user. You can also get the user's questions, followers, and followings by replacing 'responses' with 'questions', 'followers', or 'followings' in the URL.",
            "needToken": True,
            "bodyJson": {},
            "responseJson": [
                {
                    "id": "int (NOT NULL)",
                    "created_at": "string (NOT NULL)",
                    "content": "string (NOT NULL)",
                    "author": "int (NOT NULL)",
                    "upvote_count": "int (NOT NULL)",
                    "downvote_count": "int (NOT NULL)",
                    "question": "int (NOT NULL)"
                }
            ]
        },
        {
            "title": "Get followers or followings of one user",
            "method": "GET",
            "url": "api/user/{id}/{followers or followings}",
            "description": "Fetches all followers of a specific user. You can also get the user's questions, responses, and followings by replacing 'followers' with 'questions', 'responses', or 'followings' in the URL.",
            "needToken": True,
            "bodyJson": {},
            "responseJson": [
                {
                    "image":"string (NULL)",
                    "first_name": "string (NOT NULL)",
                    "last_name": "string (NOT NULL)",
                    "id": "int (NOT NULL)",
                    "last_login": "string",
                    "is_superuser": "boolean (NOT NULL)",
                    "email": "string (NOT NULL)",
                    "is_staff": "boolean (NOT NULL)",
                    "username": "string (NOT NULL)",
                    "questions_count": "int (NOT NULL)",
                    "themes_count": "int (NOT NULL)",
                    "votes_count": "int (NOT NULL)",
                    "responses_count": "int (NOT NULL)",
                    "followers_count": "int (NOT NULL)",
                    "followings_count": "int (NOT NULL)"
                }
            ]
        }

        , {
            "title": "Get profile",
            "method": "GET",
            "url": "api/profile",
            "description": "Fetches the basic details of the currently authenticated user. Additional requests are needed to retrieve detailed information such as questions, responses, followers, and followings.",
            "needToken": True,
            "bodyJson": {},
            "responseJson": {
                    "image":"string (NULL)",
                "first_name": "string (NULL)",
                "last_name": "string (NULL)",
                "id": "int (NOT NULL)",
                "last_login": "datetime (NULL)",
                "is_superuser": "boolean (NOT NULL)",
                "email": "string (NOT NULL)",
                "is_staff": "boolean (NOT NULL)",
                "username": "string (NOT NULL)",
                "questions_count": "int (NOT NULL)",
                "themes_count": "int (NOT NULL)",
                "votes_count": "int (NOT NULL)",
                "responses_count": "int (NOT NULL)",
                "followers_count": "int (NOT NULL)",
                "followings_count": "int (NOT NULL)"
            }

        },
        {
            "title": "Get detail of current user",
            "method": "GET",
            "url": "api/profile/questions",
            "description": "Fetches all questions of a specific user. You can also get the user's responses, followers, and followings by replacing 'questions' with 'responses', 'followers', or 'followings' in the URL.",
            "needToken": True,
            "bodyJson": {},
            "responseJson": [
                {
                    "id": "int (NOT NULL)",
                    "created_at": "string (NOT NULL)",
                    "content": "string (NOT NULL)",
                    "author": "int (NOT NULL)",
                    "themes": [
                        "int (NOT NULL)"
                    ],
                    "isValidate": "boolean (NOT NULL)",
                    "responses_count": "int (NOT NULL)"
                }
            ]
        }, {
            "title": "Get detail of current user",
            "method": "GET",
            "url": "api/profile/responses",
            "description": "Fetches all responses of a specific user. You can also get the user's questions, followers, and followings by replacing 'responses' with 'questions', 'followers', or 'followings' in the URL.",
            "needToken": True,
            "bodyJson": {},
            "responseJson": [
                {
                    "id": "int (NOT NULL)",
                    "created_at": "string (NOT NULL)",
                    "content": "string (NOT NULL)",
                    "author": "int (NOT NULL)",
                    "upvote_count": "int (NOT NULL)",
                    "downvote_count": "int (NOT NULL)",
                    "question": "int (NOT NULL)"
                }
            ]
        },
        {
            "title": "Get detail of current user",
            "method": "GET",
            "url": "api/profile/{followers or followings}",
            "description": "Fetches all followers of a specific user. You can also get the user's questions, responses, and followings by replacing 'followers' with 'questions', 'responses', or 'followings' in the URL.",
            "needToken": True,
            "bodyJson": {},
            "responseJson": [
                {
                    "image":"string (NULL)",
                    "first_name": "string (NOT NULL)",
                    "last_name": "string (NOT NULL)",
                    "id": "int (NOT NULL)",
                    "last_login": "string",
                    "is_superuser": "boolean (NOT NULL)",
                    "email": "string (NOT NULL)",
                    "is_staff": "boolean (NOT NULL)",
                    "username": "string (NOT NULL)",
                    "questions_count": "int (NOT NULL)",
                    "themes_count": "int (NOT NULL)",
                    "votes_count": "int (NOT NULL)",
                    "responses_count": "int (NOT NULL)",
                    "followers_count": "int (NOT NULL)",
                    "followings_count": "int (NOT NULL)"
                }
            ]
        },

        {
            "title": "Edit profile",
            "method": "PUT",
            "url": "api/profile",
            "description": "Modifies the user's profile by changing their username, first name, and last name, without modifying the email or password.",
            "needToken": True,
            "bodyJson": {
                "username": "string (NOT NULL)",
                "first_name": "string (NOT NULL)",
                "last_name": "string (NOT NULL)"
            },
            "responseJson": {
                    "image":"string (NULL)",
                "first_name": "string (NOT NULL)",
                "last_name": "string (NOT NULL)",
                "id": "int (NOT NULL)",
                "last_login": "string",
                "is_superuser": "boolean (NOT NULL)",
                "email": "string (NOT NULL)",
                "is_staff": "boolean (NOT NULL)",
                "username": "string (NOT NULL)",
                "questions_count": "int (NOT NULL)",
                "themes_count": "int (NOT NULL)",
                "votes_count": "int (NOT NULL)",
                "responses_count": "int (NOT NULL)",
                "followers_count": "int (NOT NULL)",
                "followings_count": "int (NOT NULL)"
            }
        }
        , {
            "title": "Delete profile",
            "method": "DELETE",
            "url": "api/profile",
            "description": "Deletes the user's profile. Currently, this action removes the user's account and all associated data. In the future, questions, responses, and other data will be associated with a 'deleted' user instead of being completely removed.",
            "needToken": True,
            "bodyJson": {},
            "responseJson": {}
        }, {
            "title": "Upload image",
            "method": "PATCH",
            "url": "api/upload/image/to/profile",
            "description": "You can add your own profile image to custom your profile.You can get image url in your profile data. Create a formdata with file associated to key <image>",
            "needToken": True,
            "bodyJson": {},
            "responseJson": {}
        }

    ]
