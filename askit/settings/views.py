import json

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from home_page.models import Question, Answer, Comment, UserProfile


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def delete_account(request):
    if request.method == 'DELETE':
        # load the json data
        delete_data = json.loads(request.body)
        should_delete_content = delete_data['should_delete_content']
        user = request.user

        if should_delete_content:
            # delete all questions from the user
            questions = Question.objects.filter(author=user)
            for question in questions:
                question.delete()
            # delete all answers from the user
            answers = Answer.objects.filter(author=user)
            for answer in answers:
                answer.delete()
            # delete all comments from the user
            comments = Comment.objects.filter(author=user)
            for comment in comments:
                comment.delete()

        user.delete()
        return JsonResponse({'message': 'Account deleted successfully'}, status=200)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def change_username(request):
        if request.method == 'POST':
            user = UserProfile.objects.get(user=request.user)
            post_data = json.loads(request.body)
            first_name = post_data['first_name']
            last_name = post_data['last_name']
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return JsonResponse({'first_name': first_name, 'last_name': last_name})

