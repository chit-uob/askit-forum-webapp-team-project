from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name


class Module(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=3000)
    pub_date = models.DateTimeField(auto_now_add=True)
    admins = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="module_admins")
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="module_members")

    def __str__(self):
        return self.title


class Tag(models.Model):
    tag_name = models.CharField(max_length=50)

    def __str__(self):
        return self.tag_name


class Question(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    explanation = models.CharField(max_length=3000)
    tried_what = models.CharField(max_length=500)
    summary = models.CharField(max_length=500)
    pub_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="Unanswered")
    tags = models.ManyToManyField(Tag, related_name="question_tags")
    score = models.IntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    upvotes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="question_upvotes")
    downvotes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="question_downvotes")

    def __str__(self):
        return self.title


class Answer(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=3000)
    pub_date = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0)
    upvotes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="answer_upvotes")
    downvotes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="answer_downvotes")
    is_solution = models.BooleanField(default=False)
    from_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.content


class Notification(models.Model):
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    detail = models.CharField(max_length=500)
    link = models.CharField(max_length=150, default="")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.detail


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=3000, default="")

    def __str__(self):
        return self.author


class Activity(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    action = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=150, default="")

    def __str__(self):
        return self.action
