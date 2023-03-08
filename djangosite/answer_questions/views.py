from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from home_page.models import Question, Answer

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the answer questions")


def check_upvote_or_downvote(question):
    return "upvote"


def view_question(request, question_id):
    context = {}
    try:
        question = Question.objects.get(id=question_id)
        context['question_id'] = question.id
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

        answer_query_result = Answer.objects.filter(question=question)
        context['answer_list'] = []
        for answer in answer_query_result:
            answer_dict = {}
            answer_dict['author'] = answer.author
            answer_dict['content'] = answer.content
            answer_dict['pub_date'] = answer.pub_date
            context['answer_list'].append(answer_dict)
    except Question.DoesNotExist:
        context['question_id'] = context['title'] = context['author'] = context['module'] = context['explanation'] = context['tried_what'] = context['summary'] = context['pub_date'] = context['status'] = context['score'] = context['views'] = context['upvote_or_downvote'] = "Question does not exist"
    return render(request, 'answer_questions/view_question.html', context)
    # return JsonResponse(context)


def submit_answer(request, question_id):
    if request.method == 'POST':
        question = Question.objects.get(id=question_id)
        content = request.POST.get('content')
        # don't have author yet
        # author =
        answer = Answer(question=question, content=content)
        answer.save()
        return HttpResponseRedirect(reverse('answer_questions:view_question', args=(question_id,)))