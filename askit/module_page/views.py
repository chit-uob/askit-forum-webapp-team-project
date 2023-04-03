from django.http import JsonResponse
from home_page.models import Question, Module, Answer
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
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

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def view_popular_questions(request, mod, days):
    module = Module.objects.get(title=mod)
    questions = Question.objects.filter(module=module)
    question_array = []
    for index ,question in enumerate(questions):
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
        if(index == 3):
            break

    return JsonResponse(question_array, safe=False)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def view_module_list(request):
    modules = Module.objects.all()
    module_array = []
    for module in modules:
        context = {'id': module.id,
                   'title': module.title,
                   'description': module.description,
                   }
        module_array.append(context)

    return JsonResponse(module_array, safe=False)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def is_admin(request,mod):
    the_module = Module.objects.get(title=mod)
    print(the_module.admins.all())
    if request.user in the_module.admins.all(): 
        return JsonResponse({'admin': True } )
    else:
        return JsonResponse({'admin': False } )
