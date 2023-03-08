from django.urls import path
from . import views

app_name = 'answer_questions'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.view_question, name='view_question'),
]