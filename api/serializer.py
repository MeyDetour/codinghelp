from django.template.context_processors import request
from rest_framework import serializers

from api.models import User, Question,Theme


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
        validated_data.pop('password', None)
        validated_data.pop('email', None)

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        return instance



class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id','content', 'author','theme']


class ThemeSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True, source='question_set')  # Associe toutes les questions liées

    class Meta:
        model = Theme
        fields = ['id','name','author','questions']
