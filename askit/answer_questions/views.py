import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from home_page.models import Question, Answer, Tag, Module



def check_upvote_or_downvote(question):
    return "upvote"

def view_question(request, question_id):
    context = {}
    try:
        question = Question.objects.get(id=question_id)
        question.views += 1
        question.save()
        context['question_id'] = question.id
        context['title'] = question.title
        context['author'] = question.author
        context['module'] = question.module.title
        context['explanation'] = question.explanation
        context['tried_what'] = question.tried_what
        context['summary'] = question.summary
        context['pub_date'] = question.pub_date
        context['status'] = question.status
        context['tags'] = str(question.tags.all())
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
            answer_dict['score'] = answer.score
            answer_dict['is_solution'] = answer.is_solution
            context['answer_list'].append(answer_dict)
    except Question.DoesNotExist:
        context['question_id'] = context['title'] = context['author'] = context['module'] = context['explanation'] = context['tried_what'] = context['summary'] = context['pub_date'] = context['status'] = context['score'] = context['views'] = context['upvote_or_downvote'] = "Question does not exist"
    return JsonResponse(context)


def create_question(request):
    m = Module(title="OSSP", description="ossp des")
    m.save()
    m1 = Module(title="TP", description="ossp des")
    m1.save()
    m2 = Module(title="SE", description="ossp des")
    m2.save()
    q = Question(module=m, title="how to do", explanation="exp", tried_what="tried", summary="sum")
    q.save()
    q2 = Question(module=m, title="question2", explanation="exp", tried_what="tried", summary="sum")
    q2.save()
    q3 = Question(module=m1, title="question3", explanation="exp", tried_what="tried", summary="sum")
    q3.save()
    q4 = Question(module=m2, title="question4", explanation="exp", tried_what="tried", summary="sum")
    q4.save()
    t = Tag(tag_name="Apple pie")
    t.save()
    t2 = Tag(tag_name="Banana")
    t2.save()
    q.tags.add(t)
    q.tags.add(t2)
    q2.tags.add(t)
    q3.tags.add(t)
    q4.tags.add(t)
    q.save()
    q2.save()
    q3.save()
    q4.save()
    return JsonResponse({"success": True})

@csrf_exempt
def submit_answer(request, question_id):
    if request.method == 'POST':
        question = Question.objects.get(id=question_id)
        post_data = json.loads(request.body)
        content = post_data['content']
        # todo don't have author yet
        # author =
        answer = Answer(question=question, content=content)
        answer.save()
        answer_dict = {}
        answer_dict['author'] = answer.author
        answer_dict['content'] = answer.content
        answer_dict['pub_date'] = answer.pub_date
        answer_dict['score'] = answer.score
        answer_dict['is_solution'] = answer.is_solution
        return JsonResponse(answer_dict)


@csrf_exempt
def upvote(request, question_id):
    if request.method == 'POST':
        question = Question.objects.get(id=question_id)
        question.score += 1
        question.save()
        return JsonResponse({"success": True, "score": question.score})


@csrf_exempt
def downvote(request, question_id):
    if request.method == 'POST':
        question = Question.objects.get(id=question_id)
        question.score -= 1
        question.save()
        return JsonResponse({"success": True, "score": question.score})
