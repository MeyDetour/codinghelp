from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
#
# class User(models.Model):
#     name = models.CharField(max_length=50)
#     password = models.TextField()
#     email = models.CharField(max_length=50)
#     username = None
#
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []
#
#     def __str__(self):
#         return self.name

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []



class Theme(models.Model):

    name = models.CharField(max_length=50)

    # we want to replace with and "deleted user" instead of delete question
    # we avoid to delete theme in specific function get_theme['DELETE']
    # and USER DELETE PROFIL get_theme['DELETE']
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False)

    def __str__(self):
        return self.name

class Question(models.Model):
    content = models.TextField()
    # we want to replace with and "deleted user" instead of delete question
    # we avoid to delete theme in specific function get_question['DELETE']
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING , null=False)
    themes = models.ManyToManyField(Theme, related_name="questions")  # Many-to-Many relation
    isValidate =  models.BooleanField(null=True)
    def __str__(self):
        return self.content


class Response(models.Model):
    content = models.TextField()
    question = models.ForeignKey(Question,on_delete=models.CASCADE,null=False)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    def __str__(self):
        return self.content

class UpVote(models.Model):
    response = models.ForeignKey(Response, on_delete=models.CASCADE,null=False)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    def __str__(self):
        return self.author