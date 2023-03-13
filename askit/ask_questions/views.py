from django.shortcuts import render
import json
from django.http import JsonResponse
# Create your views here.
from home_page.models import Question, Module, Tag, Answer
from django.views.decorators.csrf import csrf_exempt
import requests

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

def display_questions(request, question_id):
    dis_question = {}
    try:
        question = Question.objects.get(id=question_id)
        question.views += 1
        question.save()
        dis_question['question_id'] = question.id
        dis_question['title'] = question.title
        dis_question['author'] = question.author
        dis_question['module'] = question.module.title
        dis_question['explanation'] = question.explanation
        dis_question['tried_what'] = question.tried_what
        dis_question['summary'] = question.summary
        dis_question['pub_date'] = question.pub_date
        dis_question['status'] = question.status
        dis_question['tags'] = str(question.tags.all())
        dis_question['score'] = question.score
        dis_question['views'] = question.views
        # context['upvote_or_downvote'] = check_upvote_or_downvote(question)

        # answer_query_result = Answer.objects.filter(question=question)
        # context['answer_list'] = []
        # for answer in answer_query_result:
        #     answer_dict = {}
        #     answer_dict['author'] = answer.author
        #     answer_dict['content'] = answer.content
        #     answer_dict['pub_date'] = answer.pub_date
        #     answer_dict['score'] = answer.score
        #     answer_dict['is_solution'] = answer.is_solution
        #     context['answer_list'].append(answer_dict)
    except Question.DoesNotExist:
        dis_question['question_id'] = dis_question['title'] = dis_question['author'] = dis_question['module'] = dis_question['explanation'] = \
        dis_question['tried_what'] = dis_question['summary'] = dis_question['pub_date'] = dis_question['status'] = dis_question['score'] = \
        dis_question['views'] = dis_question['upvote_or_downvote'] = "Question does not exist"
    return JsonResponse(dis_question)

