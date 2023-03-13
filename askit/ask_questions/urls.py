from django.urls import path
from . import views

app_name = 'ask_questions'
urlpatterns = [
    path('', views.submit_question, name='submitQuestions'),
]