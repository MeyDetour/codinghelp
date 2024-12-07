from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.models import ResponseText, Vote
from api.view import is_authenticate


@api_view(['POST'])
def to_upvote_response(request, response_id):

    user = is_authenticate(request)
    if not user:
        return Response({"message": "Erreur lors de l'authentification"}, status=400)



    # assert that response exist
    response = get_object_or_404(ResponseText, pk=response_id)

    if user.id == response.author.id :
        return Response({"message": "You can't upvote your own response"}, status=400)

    try:
        precedent_vote = Vote.objects.get(response=response, author=user)
    except Vote.DoesNotExist:
        precedent_vote = None

    # if it was already voted
    if precedent_vote:
        # if it was bad voted we switch to good
        # if it's good we delete it to toggle effect

        if precedent_vote.type == "downvote":
            precedent_vote.type = "upvote"
            precedent_vote.save()
            return Response({"message": "ok"}, status=200)
        elif precedent_vote.type == "upvote":
            precedent_vote.delete()
            return Response({"message": "ok"}, status=200)

    # if it's note voted we create bad vote
    # because we are in DOWNVOTE function

    new_vote = Vote(author=user, response=response, type="upvote")
    new_vote.save()
    return Response({"message": "ok"}, status=201)


@api_view(['POST'])
def to_downvote_response(request, response_id):
    user = is_authenticate(request)
    if not user:
        return Response({"message": "Erreur lors de l'authentification"}, status=400)

    # assert that response exist
    response = get_object_or_404(ResponseText, pk=response_id)

    try:
        precedent_vote = Vote.objects.get(response=response, author=user)
    except Vote.DoesNotExist:
        precedent_vote = None

    # if it was already voted
    if precedent_vote:
        # if it was good voted we switch to bad
        # if it's bad we delete it to toggle effect

        if precedent_vote.type == "upvote":
            precedent_vote.type = "downvote"
            precedent_vote.save()
            return Response({"message": "ok"}, status=200)
        elif precedent_vote.type == "downvote":
            precedent_vote.delete()
            return Response({"message": "ok"}, status=200)

    # if it's note voted we create bad vote
    # because we are in DOWNVOTE function

    new_vote = Vote(author=user, response=response, type="downvote")
    new_vote.save()
    return Response({"message": "ok"}, status=201)
