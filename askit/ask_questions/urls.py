from django.urls import path
from . import views

app_name = 'ask_questions'
urlpatterns = [
    path('summary/', views.summary_api, name='summaryApi'),
    path('tagging/', views.tag_api, name='tagApi'),
    path('spacy/', views.spacy_tag, name='spacyTag'),
    path('module/<str:mod>/', views.submit_question, name='submitQuestions'),
]