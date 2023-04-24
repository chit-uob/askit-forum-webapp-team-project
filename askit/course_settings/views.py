import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from home_page.models import Module
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def get_details(request, mod):
    module = Module.objects.get(title=mod)
    if request.user.is_superuser or request.user in module.admins.all():
        return JsonResponse({'title': module.title, 'description': module.description}, status=200)
