from django.urls import path
from . import views

app_name = 'home_page'
urlpatterns = [
    path('notifs/', views.view_notifications, name='all_notifications'),
    path('vQuestions/', views.view_questions, name='all_questions'),
    path('vAnswers/', views.view_answers, name='user_answers')
]