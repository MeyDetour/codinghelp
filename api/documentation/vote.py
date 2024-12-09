def get_vote_routes():
    return [
        {
            "title": "To upvote response",
            "method": "PATCH",
            "url": "api/upvote/{responseId}",
            "description": "Upvotes a response. If the response is already upvoted by the user, the vote is removed (toggle functionality). This allows the user to switch between upvoting and removing the upvote.",
            "needToken": True,
            "bodyJson": {},
            "responseJson": {}
        }
        , {
            "title": "To downvote response",
            "method": "PATCH",
            "url": "api/downvote/{responseId}",
            "description": "Downvotes a response. If the response is already downvoted by the user, the vote is removed (toggle functionality). This allows the user to switch between downvoting and removing the downvote.",
            "needToken": True,
            "bodyJson": {},
            "responseJson": {}
        }]
