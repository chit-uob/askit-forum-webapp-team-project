from django.http import HttpResponse
from django.shortcuts import render
from home_page.models import Question, Answer

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the answer questions")

def view_question(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
        title = question.title
    except Question.DoesNotExist:
        title = "Question does not exist"
    return render(request, 'answer_questions/view_question.html', {'question_id': question_id, 'title': title})
