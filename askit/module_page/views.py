from django.http import JsonResponse
from home_page.models import Question, Module, Answer

# Create your views here.
def view_question_list(request, mod):
    module = Module.objects.get(title = mod)
    questions = Question.objects.filter(module = module) 
    question_array = []
    for question in questions:
        context = {}
        context['id'] = question.id
        context['title'] = question.title
        context['author'] = question.author
        context['pub_date'] = question.pub_date
        context['tags'] = []
        for x in question.tags.all():
            context['tags'].append(str(x))
        context['score'] = question.score
        context['views'] = question.views
        context['num_answers'] = Answer.objects.filter(question = question).count()
        # context['upvote'] = question.upvotes
        # context['downvote'] = question.downvotes
        question_array.append(context)

    return JsonResponse(question_array, safe=False)

