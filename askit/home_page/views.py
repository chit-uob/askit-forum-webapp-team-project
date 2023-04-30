import json
from datetime import datetime

from django.http import JsonResponse
from home_page.models import Question, UserProfile, Answer, Notification, Activity
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def view_activity(request):
    curuser = request.user
    activities = Activity.objects.filter(author=curuser)
    # filter only the activities from this month
    activities = activities.filter(date__month=datetime.now().month)
    activity_array = []
    for activity in activities:
        context = {
            'date': activity.date,
        }
        activity_array.append(context)
    return JsonResponse(activity_array, safe=False)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def view_notifications(request):
    curuser = request.user
    notifications = Notification.objects.filter(receiver=curuser)
    notification_array = []
    for notification in notifications:
        context = {'id': notification.id,
                   'receiver': getattr(notification.receiver, 'username', None),
                   'detail': notification.detail,
                   'link': notification.link,
                   'date': notification.date,
                   }
        notification_array.append(context)
    return JsonResponse(notification_array, safe=False)


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def delete_notification(request, notification_id):
    if request.method == 'DELETE':
        notification = Notification.objects.get(id=notification_id)
        notification_user = notification.receiver
        if notification_user != request.user:
            return JsonResponse({'message': 'You are not authorized to delete this notification'}, status=403)
        notification.delete()
        return JsonResponse({'message': 'Notification deleted successfully'}, status=200)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def view_questions(request):
    qUser = request.user
    questions = Question.objects.filter(author=qUser)
    question_array = []
    for question in questions:
        context = {'id': question.id,
                   'module': question.module.title,
                   'title': question.title,
                   'pub_date': question.pub_date,
                   'tags': [tag.tag_name for tag in question.tags.all()],
                   'score': question.score,
                   'views': question.views,
                   'status': question.status,
                   'answers_count': question.answer_set.count(),
                   }
        question_array.append(context)

    return JsonResponse(question_array, safe=False)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def view_answers(request):
    aUser = request.user
    answers = Answer.objects.filter(author=aUser)
    answer_array = []
    for answer in answers:
        question_of_answer = answer.question
        context = {
            'id': answer.id,
            'question_id': question_of_answer.id,
            'question_title': question_of_answer.title,
            'author': getattr(question_of_answer.author, 'username', 'Anonymous'),
            'content': answer.content,
            'pub_date': answer.pub_date,
            'score': answer.score,
            'is_solution': answer.is_solution,
        }
        answer_array.append(context)

    return JsonResponse(answer_array, safe=False)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_profiles(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    context = {
        'username': user.username,
        'full_name': user_profile.get_full_name(),
    }
    return JsonResponse(context, safe=False)


#         questions = Question.objects.all()
#         question_list = []
#         for question in questions:
#             question_data = {
#                 'id': question.id,
#                 'author': question.author.username,
#                 'module': question.module.title,
#                 'title': question.title,
#                 'explanation': question.explanation,
#                 'tried_what': question.tried_what,
#                 'summary': question.summary,
#                 'pub_date': question.pub_date,
#                 'status': question.status,
#                 'tags': [tag.tag_name for tag in question.tags.all()],
#                 'score': question.score,
#                 'views': question.views,
#                 'upvotes': [user.username for user in question.upvotes.all()],
#                 'downvotes': [user.username for user in question.downvotes.all()],
#                 # 'answers': [{
#                 #     'id': answer.id,
#                 #     'author': answer.author.username,
#                 #     'content': answer.content,
#                 #     'pub_date': answer.pub_date,
#                 #     'score': answer.score,
#                 #     'is_solution': answer.is_solution,
#                 #     'upvotes': [user.username for user in answer.upvotes.all()],
#                 #     'downvotes': [user.username for user in answer.downvotes.all()]
#                 # } for answer in question.answer_set.all()]
#             }
#             question_list.append(question_data)
#
#         return JsonResponse(question_list, safe=False)
#
# @api_view(['GET'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
#
# def view_answers(request, question_id):
#     question = Question.objects.get(id=question_id)
#     answers = Answer.objects.filter(question=question).order_by('-is_solution', '-score')
#     answer_list = []
#     for answer in answers:
#         context = {'id': answer.id,
#                    'author': answer.author.get_full_name(),
#                    'content': answer.content,
#                    'pub_date': answer.pub_date,
#                    'score': answer.score,
#                    'is_solution': answer.is_solution
#                    }
#         answer_list.append(context)
#
#     return JsonResponse(answer_list, safe=False)
# Create your views here.
# @csrf_exempt
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def userInfo(request):
    if request.method == 'GET':
        post_data = json.loads(request.body)
        userName = post_data['username']
        first_name = post_data['first_name']
        last_name = post_data['last_name']
        user = User.objects.get(username=userName)
        profile = UserProfile.objects.create(user=user, first_name=first_name, last_name=last_name)
        profile.save()
        return JsonResponse({"success": True})
