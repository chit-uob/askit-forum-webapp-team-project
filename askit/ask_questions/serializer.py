from rest_framework import serializers
from home_page import Question, Module

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields=("author","module","title","explanation","tried_what","summary","pub_date","status","tags","score","views","upvotes","downvotes")