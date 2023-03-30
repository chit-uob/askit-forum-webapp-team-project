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
        m.admins.add(request.user)
        return JsonResponse({'title': title, 'description': description})
@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def delete_module(request, mod):
    if request.method == 'DELETE':
        the_module = Module.objects.get(title=mod)
        # check if request.user is in the_module.admins
        if request.user in the_module.admins.all():
            the_module.delete()
            return JsonResponse({'message': f'{mod} deleted'})
        else:
            return JsonResponse({'message': 'you are not authorized to delete this module'})