from django.http import JsonResponse
from home_page.models import Question, Module, Answer


# Create your views here.
def view_question_list(request, mod):
    module = Module.objects.get(title=mod)
    questions = Question.objects.filter(module=module)
    question_array = []
    for question in questions:
        context = {'id': question.id,
                   'title': question.title,
                   'author': getattr(question.author, 'username', None),
                   'pub_date': question.pub_date,
                   'tags': []
                   }
        for tag_name in question.tags.all():
            context['tags'].append(str(tag_name))
        context['score'] = question.score
        context['views'] = question.views
        context['num_answers'] = Answer.objects.filter(question=question).count()
        question_array.append(context)

    return JsonResponse(question_array, safe=False)
