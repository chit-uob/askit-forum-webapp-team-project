from django.shortcuts import render
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from home_page.models import UserProfile
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def addName(request):
    if request.method == 'POST':
        post_data = json.loads(request.body)
        userName = post_data['username']
        first_name = post_data['first_name']
        last_name = post_data['last_name']
        user = User.objects.get(username=userName)
        profile = UserProfile.objects.create(user=user,first_name=first_name,last_name=last_name)
        profile.save()
        return JsonResponse({"success": True})


