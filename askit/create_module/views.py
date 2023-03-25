import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from home_page.models import Module


@csrf_exempt
def new_module(request):
    if request.method == 'POST':
        post_data = json.loads(request.body)
        title = post_data['title']
        description = post_data['description']
        m = Module(title=title, description=description)
        m.save()
        return JsonResponse({"success": True})