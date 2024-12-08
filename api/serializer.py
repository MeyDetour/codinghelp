from crypt import methods
from math import trunc

from django.template.context_processors import request
from rest_framework import serializers

from api.models import User, Question, Theme, Vote,ResponseText


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name',"last_name",'password','id',"last_login","is_superuser","email","is_staff","username"]
        extra_kwargs={
            "password":{'write_only':True,"required":False},
            "email":{'required':False}
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


class UserDetailsSerializer(serializers.ModelSerializer):
    questions_count= serializers.SerializerMethodField()
    responses_count= serializers.SerializerMethodField()
    themes_count= serializers.SerializerMethodField()
    votes_count= serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['first_name',"last_name",'password','id',"last_login","is_superuser","email","is_staff","username","questions_count","themes_count","votes_count","responses_count","followers","following"]
        extra_kwargs={
            "password":{'write_only':True,"required":False},
            "email":{'required':False}
        }

    def get_questions_count(self,obj):
        return obj.questions.count()
    def get_themes_count(self,obj):
        return obj.themes.count()
    def get_responses_count(self,obj):
        return obj.responses.count()
    def get_votes_count(self,obj):
        return obj.votes.count()


class QuestionSerializer(serializers.ModelSerializer):
    themes = serializers.PrimaryKeyRelatedField(many=True, queryset=Theme.objects.all())  # Utiliser les IDs des thèmes
    responses_count = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ['id','content', 'author','themes','isValidate','responses_count']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['isValidate'] = data['isValidate'] if data['isValidate'] is not None else False
        return data
    def get_responses_count(self, obj):
        return obj.responses.count()

class QuestionDetailsSerializer(serializers.ModelSerializer):
    themes = serializers.PrimaryKeyRelatedField(many=True, queryset=Theme.objects.all())  # Utiliser les IDs des thèmes
    responses = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ['id','content', 'author','themes','isValidate','responses']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['isValidate'] = data['isValidate'] if data['isValidate'] is not None else False
        return data

    def get_responses(self, obj):
        responses = obj.responses.all()  # Utilisation du related_name défini dans Response
        return ResponseSerializer(responses, many=True).data

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

    class Meta:
        model = ResponseText
        fields = ['id', 'content', 'author', 'upvote_count','downvote_count',"question"]

    def get_upvote_count(self, obj):
        return obj.votes.filter(type="upvote").count()

    def get_downvote_count(self, obj):
        return obj.votes.filter(type="downvote").count()

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