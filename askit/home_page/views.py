from django.http import JsonResponse
from home_page.models import Question, UserProfile, Answer, Notification
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])

def view_notifications(request):
    curuser = request.user
    notifications = Notification.objects.filter(receiver=curuser)
    notification_array = []
    for notification in notifications:
        context = {'id': notification.id,
                   'receiver': notification.receiver,
                   'detail': notification.detail,
                   'link': notification.link,
                   'date': notification.link,
                   }
        notification_array.append(context)

        return JsonResponse(notification_array, safe=False)
