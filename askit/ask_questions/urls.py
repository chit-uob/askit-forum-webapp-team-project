from django.urls import path
from . import views

app_name = 'ask_questions'
urlpatterns = [
#     path('', views.index, name='index'),
    path('ask/<int:question_id>/', views.display_questions, name='display_question'),
#     path('<int:question_id>/submit_question/', views.submit_question, name='submit_question'),
#     path('<int:question_id>/upvote/', views.upvote, name='upvote'),
#     path('<int:question_id>/downvote/', views.downvote, name='downvote'),
#     path('create_question/', views.create_question, name='create_question'),
]