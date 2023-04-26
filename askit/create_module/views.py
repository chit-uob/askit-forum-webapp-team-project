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
        title = post_data['title']
        description = post_data['explanation']
        m = Module(title=title, description=description)
        m.save()
        m.admins.add(request.user)
        m.members.add(request.user)
        m.save()
        return JsonResponse({'title': title, 'description': description})

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def delete_module(request, mod):
    if request.method == 'DELETE':
        m = Module.objects.get(title=mod)
        if request.user.is_superuser or request.user in m.admins.all():
            m.delete()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'You are not an admin'})

