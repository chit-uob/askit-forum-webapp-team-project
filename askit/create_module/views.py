import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from home_page.models import Module
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def new_module(request):
    if request.method == 'POST':
        post_data = json.loads(request.body)
        print(post_data)
        title = post_data['title']
        description = post_data['explanation']
        m = Module(title=title, description=description)
        m.save()
        return JsonResponse({'title': title, 'description': description})