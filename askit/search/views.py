from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from home_page.models import Question, Module, Tag, Answer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def search_questions(request):
    if request.method == 'GET':
        search_term = request.GET['searchTerm']
        if 'module' in request.GET:
            module = request.GET['module']
            result_search = Module.objects.get(title=module)
            search_results = Question.objects.filter( title__icontains=search_term).filter(module=result_search)

            question_array = []
            for question in search_results:
                context = {'id': question.id,
                        'title': question.title,
                        'author': getattr(question.author, 'username', 'Anonymous'),
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
            
        else:
            search_results = Question.objects.filter(title__icontains=search_term)
            question_array = []
            for question in search_results:
                context = {'id': question.id,
                           'title': question.title,
                           'author': getattr(question.author, 'username', 'Anonymous'),
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


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def advanced_search(request):
    # todo: implement advanced search

    if request.method == 'GET':
        adv_result = Question.objects.all() 
        if 'titleContains' in request.GET:
            titleContains = request.GET['titleContains']
            adv_result = adv_result.filter(title__icontains=titleContains)

        if 'contentContains' in request.GET:
            contentContains = request.GET['contentContains']
            adv_result = adv_result.filter(explanation__icontains=contentContains)

        if 'course' in request.GET:
            course = request.GET['course']
            adv_module_search = Module.objects.get(title=course)
            adv_result = adv_result.filter(module=adv_module_search)

        if 'containTags' in request.GET:
            containTags = request.GET['containTags']
            tag_result = Tag.objects.filter(tag_name=containTags)
            adv_result = adv_result.filter(tags__in=tag_result)
        
        question_array = []
        for question in adv_result:
            context = {'id': question.id,
                    'title': question.title,
                    'author': getattr(question.author, 'username', 'Anonymous'),
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
