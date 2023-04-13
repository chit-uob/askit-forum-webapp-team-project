import json

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from home_page.models import Question, Answer, Comment


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
            print("delete content")
            # # delete all questions from the user
            # questions = Question.objects.filter(author=user)
            # for question in questions:
            #     question.delete()
            # # delete all answers from the user
            # answers = Answer.objects.filter(author=user)
            # for answer in answers:
            #     answer.delete()
            # # delete all comments from the user
            # comments = Comment.objects.filter(author=user)
            # for comment in comments:
            #     comment.delete()

        # user.delete()
        print("delete user: ", user.username)
        return JsonResponse({'message': 'Account deleted successfully'}, status=200)