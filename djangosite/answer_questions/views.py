from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the answer questions")

def view_question(request, question_id):
    return render(request, 'answer_questions/view_question.html', {'question_id': question_id})