from math import trunc

from django.template.context_processors import request
from rest_framework import serializers

from api.models import User, Question, Theme, UpVote,Response


class UserSerializer(serializers.ModelSerializer):
    question_count= serializers.IntegerField(source="question_set.count",read_only=True)

    class Meta:
        model = User
        fields = ['first_name',"last_name",'password','id',"last_login","is_superuser","email","is_staff","username","question_count"]
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
        validated_data.pop('password', None)
        validated_data.pop('email', None)

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        return instance



class QuestionSerializer(serializers.ModelSerializer):
    themes = serializers.PrimaryKeyRelatedField(many=True, queryset=Theme.objects.all())  # Utiliser les IDs des thèmes

    class Meta:
        model = Question
        fields = ['id','content', 'author','themes','isValidate']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['isValidate'] = data['isValidate'] if data['isValidate'] is not None else False
        return data
class UpvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpVote
        fields = []

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['isValidate'] = data['isValidate'] if data['isValidate'] is not None else False
        return data


class ResponseSerializer(serializers.ModelSerializer):
    upvote_count = serializers.SerializerMethodField()

    class Meta:
        model = Response
        fields = ['id', 'content', 'author', 'upvote_count']

    def get_upvote_count(self, obj):
        return obj.upvotes.count()

class ThemeDetailSerializer(serializers.ModelSerializer):
    #pour les relations many to one
    #questions = QuestionSerializer(many=True, read_only=True, source='question_set')

    # pour le many to many
    questions = serializers.SerializerMethodField()

    class Meta:
        model = Theme
        fields = ['id', 'name', 'author', 'questions']


    def get_questions(self, obj):
        # Récupère toutes les questions associées au thème
        questions = obj.questions.all()
        return QuestionSerializer(questions, many=True).data

class ThemeListSerializer(serializers.ModelSerializer):
    question_count = serializers.IntegerField(source='question_set.count', read_only=True)
    # ajotuer apres le nombre de personne ayant participé

    class Meta:
        model = Theme
        fields = ['id', 'name', 'author', 'question_count']