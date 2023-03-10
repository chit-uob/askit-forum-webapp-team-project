from django.http import JsonResponse
from home_page.models import Question, Module

# Create your views here.
def view_question_list(request, mod):
    module = Module.objects.get(title = mod)
    questions = Question.objects.filter(module = module) 
    question_array = []
    for question in questions:
        context = {}
        context['question_id'] = question.id
        context['title'] = question.title
        context['author'] = question.author
        context['pub_date'] = question.pub_date
        context['tags'] = list(question.tags.all())
        context['score'] = question.score
        context['views'] = question.views
        context['upvote'] = question.upvotes
        context['downvote'] = question.downvotes
        question_array.append(context)

    return JsonResponse(context)

