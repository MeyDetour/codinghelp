from crypt import methods
from math import trunc

from django.template.context_processors import request
from rest_framework import serializers

from api.models import User, Question, Theme, Vote,ResponseText

representation_of_time="%d.%m.%Y"




class QuestionSerializer(serializers.ModelSerializer):
    themes = serializers.PrimaryKeyRelatedField(many=True, queryset=Theme.objects.all())  # Utiliser les IDs des thèmes
    responses_count = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    contributor_count = serializers.SerializerMethodField()
    class Meta:
        model = Question
        fields = ['id','created_at', "title",'author','themes','isValidate','responses_count','contributor_count']

    def get_contributor_count(self, obj):
         # get all authors of responsens
        answerers = obj.responses.values_list('author', flat=True).distinct()
        return len(answerers)+1
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['isValidate'] = data['isValidate'] if data['isValidate'] is not None else False
        return data
    def get_responses_count(self, obj):
        return obj.responses.count()
    def get_created_at(self,obj):
        if obj.created_at:
            return obj.created_at.strftime(representation_of_time)  # Exemple : '09/12/2024'
        return None

class QuestionDetailsSerializer(serializers.ModelSerializer):
    themes = serializers.PrimaryKeyRelatedField(many=True, queryset=Theme.objects.all())  # Utiliser les IDs des thèmes
    responses = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    contributor_count = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ['id',"created_at",'content','contentHTML', 'author','themes','isValidate','responses','title',"contributor_count"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['isValidate'] = data['isValidate'] if data['isValidate'] is not None else False
        return data

    def get_contributor_count(self, obj):
        # get all authors of responsens
        answerers = obj.responses.values_list('author', flat=True).distinct()

        return len(answerers)+1
    def get_responses(self, obj):
        responses = obj.responses.all()  # Utilisation du related_name défini dans Response
        return ResponseSerializer(responses, many=True).data
    def get_created_at(self,obj):
        if obj.created_at:
            return obj.created_at.strftime(representation_of_time)  # Exemple : '09/12/2024'
        return None
    def get_author(self,obj):
        author = obj.author  # Utilisation du related_name défini dans Response
        return UserSerializerWithoutDetail(author).data

    def create(self, validated_data):
        author = validated_data.pop('author', None)
        question = Question.objects.create(**validated_data)
        if author:
            question.author = author
            question.save()
        return question

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = []

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['isValidate'] = data['isValidate'] if data['isValidate'] is not None else False
        return data


class ResponseSerializer(serializers.ModelSerializer):
    upvote_count = serializers.SerializerMethodField()
    downvote_count = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    author_data = serializers.SerializerMethodField()
    question_data = serializers.SerializerMethodField()
    class Meta:
        model = ResponseText
        fields = ['id','created_at', 'content', 'author', 'author_data', 'upvote_count','downvote_count',"question","question_data"]

    def get_upvote_count(self, obj):
        return obj.votes.filter(type="upvote").count()

    def get_downvote_count(self, obj):
        return obj.votes.filter(type="downvote").count()

    def get_created_at(self,obj):
        if obj.created_at:
            return obj.created_at.strftime(representation_of_time)  # Exemple : '09/12/2024'
        return None

    def get_author_data(self, obj):
        author = obj.author  # Utilisation du related_name défini dans Response
        return UserSerializerWithoutDetail(author).data
    def get_question_data(self, obj):
            question = obj.question  # Utilisation du related_name défini dans Response
            return QuestionSerializer(question).data


class ThemeDetailSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    class Meta:
        model = Theme
        fields = ['id', 'name', 'author', 'questions']


    def get_questions(self, obj):
        # Récupère toutes les questions associées au thème
        questions = obj.questions.all()
        return QuestionSerializer(questions, many=True).data

class ThemeListSerializer(serializers.ModelSerializer):
    questions_count = serializers.SerializerMethodField()


    #number of people that contribuate to this project
    contributor_count = serializers.SerializerMethodField()
    class Meta:
        model = Theme
        fields = ['id', 'name', 'author', 'questions_count',"contributor_count"]

    def get_questions_count(self,obj):
        return obj.questions.count()
    def get_contributor_count(self,obj):
        # chatgpt mais j'ai compris !

        # Récupérer les auteurs distincts des questions liées au thème
        contributors = obj.questions.values_list('author', flat=True).distinct()

        # Récupérer les auteurs distincts des réponses des questions liées au thème
        answerers = obj.questions.values_list('responses__author', flat=True).distinct()

        # Combine les deux ensembles d'auteurs (questions et réponses)
        # Utiliser `union` pour garantir que les auteurs ne soient comptés qu'une seule fois
        all_contributors = set(contributors).union(set(answerers))

        # Retourner le nombre total de contributeurs uniques
        return len(all_contributors)






class UserSerializerWithoutDetail(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username','id', "image","created_at"]

    def get_created_at(self, obj):
        if obj.created_at:
            return obj.created_at.strftime(representation_of_time)  # Exemple : '09/12/2024'


class UserSerializer(serializers.ModelSerializer):
    questions_count = serializers.SerializerMethodField()
    responses_count = serializers.SerializerMethodField()
    themes_count = serializers.SerializerMethodField()
    votes_count = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()
    followings_count = serializers.SerializerMethodField()

    created_at = serializers.SerializerMethodField()

    class Meta:
            model = User
            fields = ['password','id',"last_login","is_superuser","email" ,"username","questions_count","themes_count","votes_count","responses_count","followers_count","followings_count","image","created_at"]
            extra_kwargs={
                "password":{'write_only':True,"required":False},
                "email":{'required':False},

                 }



    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


    def update(self, instance, validated_data):
        # avoid edit password and email
        validated_data.pop('password', None)
        validated_data.pop('email', None)

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        return instance

    def get_created_at(self, obj):
        if obj.created_at:
            return obj.created_at.strftime(representation_of_time)  # Exemple : '09/12/2024'

    def get_questions_count(self, obj):
        return obj.questions.count()

    def get_themes_count(self, obj):
        return obj.themes.count()

    def get_responses_count(self, obj):
        return obj.responses.count()

    def get_votes_count(self, obj):
        return obj.votes.count()
    def get_followers_count(self, obj):
        return obj.followers.count()
    def get_followings_count(self, obj):
        return obj.followings.count()


