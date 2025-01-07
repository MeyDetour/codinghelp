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

    # to set user to admin you must change row in db you cant do this with interface or function
    # super user can delete all question an all responses

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    followings = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',  # Liste des abonnés de cet utilisateur
        blank=True
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []



class Theme(models.Model):

    name = models.CharField(max_length=50)


    # we want to replace with and "deleted user" instead of delete question
    # we avoid to delete theme in specific function get_theme['DELETE']
    # and USER DELETE PROFIL get_theme['DELETE']
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True,related_name="themes")

    def __str__(self):
        return self.name

class Question(models.Model):
    content = models.TextField()
    title = models.CharField(max_length=200)
    # we want to replace with and "deleted user" instead of delete question
    # we avoid to delete theme in specific function get_question['DELETE']
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING , null=True,related_name="questions")
    themes = models.ManyToManyField(Theme, related_name="questions")  # Many-to-Many relation
    created_at = models.DateTimeField(auto_now_add=True)

    #question is set validate if there are less than 2 response and more than 500upvote on one response
    isValidate =  models.BooleanField(null=True)
    def __str__(self):
        return self.content


#Appelé responseText plutot que Response car elle entre en conflit avec la classe de DRF
class ResponseText(models.Model):
    content = models.TextField()
    question = models.ForeignKey(Question,on_delete=models.CASCADE,null=False,related_name="responses")
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="responses")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

class Vote(models.Model):
    response = models.ForeignKey(ResponseText, on_delete=models.CASCADE,null=False,related_name="votes")
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="votes")
    type = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.author} - {self.type} - {self.response}"