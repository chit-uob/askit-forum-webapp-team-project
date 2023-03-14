from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponseRedirect
# Create your views here.
from home_page.models import Question, Module, Tag, Answer
from django.views.decorators.csrf import csrf_exempt
import oneai


oneai.api_key = "042258be-d1e8-4bd0-9df1-ce48677e096d"

@csrf_exempt
def submit_question(request, mod):
    if request.method == 'POST':
        # question = Question.objects.get(id=question_id)
        post_data = json.loads(request.body)
        title = post_data['title']
        explanation = post_data['explanation']
        tried_what = post_data['tried']
        summary = post_data['summary']
        tags_str = str(post_data['tags'])
        tags = tags_str.split(',')
        module = Module.objects.get(title=mod)
        q = Question(module=module, title=title, explanation=explanation, tried_what=tried_what, summary=summary)
        q.save()
        for tag in tags:
            tag = tag.strip()
            t = Tag.objects.get_or_create(tag_name=tag)
            t[0].save()
            q.tags.add(t[0])
        q.save()
        id = q.id
        return JsonResponse({"success": True, "id": id})



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

@csrf_exempt
def summry_api(request):
    post_data = json.loads(request.body)
    text = post_data['explanation']
    summary = ""
    pipeline = oneai.Pipeline(
        steps=[
            oneai.skills.Summarize(),
        ]
    )
    output = pipeline.run(text)
    summary = output.summary.text
    return JsonResponse({"summary": summary})

@csrf_exempt
def tag_api(request):
    post_data = json.loads(request.body)
    text = post_data['explanation']
    tag = []
    pipeline = oneai.Pipeline(
        steps=[
            oneai.skills.Topics(),
        ]
    )
    output = pipeline.run(text)
    tag = output.topics.values
    return JsonResponse({"tag": tag})

def addToCluster(text):
  collection = oneai.clustering.Collection("questions")
  collection.add_items(text)