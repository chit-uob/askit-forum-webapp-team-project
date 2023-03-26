import json
from django.http import JsonResponse
from home_page.models import Question, Module, Tag, Answer
from django.views.decorators.csrf import csrf_exempt
from ask_questions.aiAPI import text_to_summary, text_to_tag_array, add_to_cluster, spacy_tag
import spacy # install spacy
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def submit_question(request, mod):
    if request.method == 'POST':
        post_data = json.loads(request.body)
        title = post_data['title'][:150]
        explanation = post_data['explanation'][:3000]
        tried_what = post_data['tried'][:500]
        summary = post_data['summary'][:500]
        tags_str = str(post_data['tags'])
        tags = tags_str.split(',')
        for i in range(len(tags)):
            tags[i] = tags[i].strip().lower()[:50]
        module = Module.objects.get(title=mod)
        author = request.user
        q = Question(module=module, title=title, explanation=explanation, tried_what=tried_what, summary=summary, author=author)
        q.save()
        for tag in tags:
            tag = tag.strip()
            t = Tag.objects.get_or_create(tag_name=tag)
            t[0].save()
            q.tags.add(t[0])
        q.save()
        question_id = q.id
        return JsonResponse({"success": True, "id": question_id})

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def summary_api(request):
    post_data = json.loads(request.body)
    text = post_data['explanation']
    return JsonResponse({"summary": text_to_summary(text)})

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
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