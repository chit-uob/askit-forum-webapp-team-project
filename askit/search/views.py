from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from home_page.models import Question, Module, Tag, Answer


@csrf_exempt
def search_questions(request):
    if request.method == 'GET':
        search_term = request.GET['searchTerm']
        if 'module' in request.GET:
            module = request.GET['module']
            # todo: implement search for a specific module
            # todo start dummy code, the following code is for searching all modules, not just one
            search_results = Question.objects.filter(title__icontains=search_term)
            question_array = []
            for question in search_results:
                context = {'id': question.id,
                           'title': question.title,
                           'author': question.author,
                           'pub_date': question.pub_date,
                           'tags': [],
                           'module': question.module.title
                           }
                for tag_name in question.tags.all():
                    context['tags'].append(str(tag_name))
                context['score'] = question.score
                context['views'] = question.views
                context['num_answers'] = Answer.objects.filter(question=question).count()
                question_array.append(context)
            return JsonResponse(question_array, safe=False)
            # todo end dummy code, please remove this when you implement the above todo
        else:
            search_results = Question.objects.filter(title__icontains=search_term)
            question_array = []
            for question in search_results:
                context = {'id': question.id,
                           'title': question.title,
                           'author': question.author,
                           'pub_date': question.pub_date,
                           'tags': [],
                           'module': question.module.title
                           }
                for tag_name in question.tags.all():
                    context['tags'].append(str(tag_name))
                context['score'] = question.score
                context['views'] = question.views
                context['num_answers'] = Answer.objects.filter(question=question).count()
                question_array.append(context)
            return JsonResponse(question_array, safe=False)


def advanced_search(request):
    # todo: implement advanced search
    return JsonResponse([], safe=False)
