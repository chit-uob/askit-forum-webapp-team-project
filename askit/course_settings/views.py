import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from home_page.models import Module
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.
def course_settings(request):
    return JsonResponse({})