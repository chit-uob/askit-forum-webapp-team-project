import json
from django.http import JsonResponse
from home_page.models import Question, Module, Tag, Answer
from django.views.decorators.csrf import csrf_exempt
from ask_questions.aiAPI import text_to_summary, text_to_tag_array, add_to_cluster, spacy_tag
import spacy # install spacy
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# loads nlp here so it doesn't have to be loaded every time a request is made
nlp = spacy.load('en_core_web_sm')

def handle_tag_string(tag_string):
    tags = tag_string.split(',')
    for i in range(len(tags)):
        tag_text = tags[i].strip().lower()[:50]
        if tag_text == '':
            continue
        tags[i] = tag_text
    return tags


def get_similarity_rating(text1, text2):
    doc1 = nlp(text1)
    doc2 = nlp(text2)
    return doc1.similarity(doc2)


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
        tags = handle_tag_string(tags_str)
        module = Module.objects.get(title=mod)
        author = request.user
        q = Question(module=module, title=title, explanation=explanation, tried_what=tried_what, summary=summary, author=author)
        q.save()
        for tag in tags:
            t = Tag.objects.get_or_create(tag_name=tag)
            t[0].save()
            q.tags.add(t[0])
        q.save()
        question_id = q.id
        return JsonResponse({"success": True, "id": question_id})

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def summary_api(request):
    post_data = json.loads(request.body)
    text = post_data['explanation']
    return JsonResponse({"summary": text_to_summary(text)})

@api_view(['POST'])
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


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def suggest(request, mod):
    post_data = json.loads(request.body)
    title = post_data['title']
    explanation = post_data['explanation']
    tags_str = str(post_data['tags'])
    tags = handle_tag_string(tags_str)
    # find all questions that contain one of the tags
    questions = Question.objects.none()
    # filter questions by module
    question_within_module = Question.objects.filter(module__title=mod)
    for tag in tags:
        questions = questions | question_within_module.filter(tags__tag_name=tag)
    # find the question with the highest similarity rating
    highest_rating = 0
    highest_question = None
    for question in questions[:100]:  # only look at the first 100 questions to save time
        # continue if one of the explanations is empty
        if question.explanation == '' or explanation == '':
            continue
        rating = get_similarity_rating(question.explanation, explanation)
        if rating > highest_rating:
            highest_rating = rating
            highest_question = question
    if highest_question is None:
        return JsonResponse({"success": False})
    else:
        return JsonResponse({"success": True, "id": highest_question.id, "title": highest_question.title, "explanation": highest_question.explanation, "tags": [str(tag) for tag in highest_question.tags.all()], "summary": highest_question.summary})
