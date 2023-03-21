import json
from django.http import JsonResponse
from home_page.models import Question, Module, Tag, Answer
from django.views.decorators.csrf import csrf_exempt
from ask_questions.aiAPI import text_to_summary, text_to_tag_array, add_to_cluster, spacy_tag
import spacy # install spacy

@csrf_exempt
def submit_question(request, mod):
    if request.method == 'POST':
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
        question_id = q.id
        return JsonResponse({"success": True, "id": question_id})


@csrf_exempt
def summary_api(request):
    post_data = json.loads(request.body)
    text = post_data['explanation']
    return JsonResponse({"summary": text_to_summary(text)})


@csrf_exempt
def tag_api(request):
    post_data = json.loads(request.body)
    text = post_data['explanation']
    return JsonResponse({"tag": text_to_tag_array(text)})

@csrf_exempt
def spacy_sim(request):
    post_data = json.loads(request.body)
    text1 = post_data['explanation']
    for question in Question.objects.all():
        text2 = question.explanation
        if spacy_tag(text1, text2) > 0.5:
            return JsonResponse(text2)
    return JsonResponse({"success": False})