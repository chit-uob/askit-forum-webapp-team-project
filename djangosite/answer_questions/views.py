from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from home_page.models import Question, Answer

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the answer questions")


def check_upvote_or_downvote(question):
    return "upvote"


def view_question(request, question_id):
    print(Question.objects.all())
    context = {}
    try:
        question = Question.objects.get(id=question_id)
        context['title'] = question.title
        context['author'] = question.author
        context['module'] = question.module.title
        context['explanation'] = question.explanation
        context['tried_what'] = question.tried_what
        context['summary'] = question.summary
        context['pub_date'] = question.pub_date
        context['status'] = question.status
        # context['tags'] = question.tags
        context['score'] = question.score
        context['views'] = question.views
        context['upvote_or_downvote'] = check_upvote_or_downvote(question)
    except Question.DoesNotExist:
        title = "Question does not exist"
    return render(request, 'answer_questions/view_question.html', context)
    # return JsonResponse(context)
