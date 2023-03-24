from django.shortcuts import render
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def addName(request):
    if request.method == 'POST':
        post_data = json.loads(request.body)
        userName = post_data['username']
        firstName = post_data['firstName']
        lastName = post_data['lastName']
        user = User.objects.get(username=userName)
        user.first_name = firstName
        user.last_name = lastName
        user.save()
        return JsonResponse({"success": True})


