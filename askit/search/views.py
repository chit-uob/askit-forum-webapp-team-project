import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from home_page.models import Question, Module, Tag, Answer


@csrf_exempt
def search_all_modules(request):
    if request.method == 'GET':
        print(request.GET['searchTerm'])
        search_term = request.GET['searchTerm']
        print(request.GET['module'])
        module = request.GET['module']
        search_results = Question.objects.filter(title__icontains=search_term)
        question_array = []
        for question in search_results:
            context = {'id': question.id,
                       'title': question.title,
                       'author': question.author,
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
    if request.method == 'POST':
        post_data = json.loads(request.body)
        search_term = post_data['searchTerm']
        search_results = Question.objects.filter(title__icontains=search_term)
        question_array = []
        for question in search_results:
            context = {'id': question.id,
                       'title': question.title,
                       'author': question.author,
                       'pub_date': question.pub_date,
                       'tags': []
                       }
            for tag_name in question.tags.all():
                context['tags'].append(str(tag_name))
            context['score'] = question.score
            context['views'] = question.views
            context['num_answers'] = Answer.objects.filter(question=question).count()
            question_array.append(context)
        return JsonResponse({"search_results": question_array}, safe=False)


def advanced_search():
    return JsonResponse({"search_results": "Advanced search not yet implemented"}, safe=False)
