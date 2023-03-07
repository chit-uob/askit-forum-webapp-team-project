import json

from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def index(request):
    names = ("bob", "dan", "jack", "lizzy", "susan")

    items = []
    for i in range(100):
        items.append({
            "name": random.choice(names),
            "age": random.randint(20, 80),
            "url": "https://example.com",
        })

    context = {}
    context["items"] = items
    context["items_json"] = json.dumps(items)

    return render(request, 'index.html', context)

def poll_home(request):
    return render(request, 'poll_home.html')