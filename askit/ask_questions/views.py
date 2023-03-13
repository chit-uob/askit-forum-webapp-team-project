from django.shortcuts import render
import json
from django.http import JsonResponse
# Create your views here.
from home_page.models import Question, Module
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def submit_question(request):
    if request.method == 'POST':
        # question = Question.objects.get(id=question_id)
        post_data = json.loads(request.body)
        content = post_data['content']
        # author =
        module = Module(module="Testing")
        module.save()
        question_dict = {}
        question_dict['author'] = Question.author
        question_dict['title'] = Question.title
        question_dict['explanation'] = Question.explanation
        question_dict['tried_what'] = Question.tried_what
        question_dict['summary'] = Question.summary
        question_dict['status'] = Question.status
        question_dict['tags'] = Question.tags
        question_dict['pub_date'] = Question.pub_date
        question_dict['score'] = Question.score
        question_dict['views'] = Question.views

        return JsonResponse(question_dict)

